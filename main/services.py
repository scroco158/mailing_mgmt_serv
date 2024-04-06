import pytz
from datetime import datetime

from django.core.mail import send_mail

from config import settings
from main.models import Sending

MY_TIME_FORMAT = '%m/%d/%Y %H:%M:%S'


def send_mailing():
    """ Рассылает сообщения по рассылкам у которых дата начала раньше
        сегодня и статус запущена всем клиентам рассылки"""

    zone = pytz.timezone('Europe/Moscow')
    current_datetime = datetime.now(zone)
    mail_from = settings.EMAIL_HOST_USER

    # print(mail_from)
    # print(settings.EMAIL_HOST_PASSWORD)

    # создание объекта с применением фильтра
    mailings = (Sending.objects.filter(start_time__lte=current_datetime)
                               .filter(status__in=['st',]))
    print('Проверка выбора рассылок и клиентов')
    print()
    for mailing in mailings:
        print(f'Активная рассылка: {mailing}')
        print(f'Клиенты по этой рассылке {[client.email for client in mailing.client.all()]}')

    for mailing in mailings:
        send_mail(
            subject=mailing.name,
            message=mailing.message.body,
            from_email=mail_from,
            recipient_list=[client.email for client in mailing.client.all()]
            )
