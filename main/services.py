import smtplib
import pytz
from datetime import datetime, timedelta
from django.core.mail import send_mail
from config import settings
from main.models import Sending, MailingAttempt

MY_TIME_FORMAT = '%m/%d/%Y %H:%M:%S'


def send_mailing():
    """ Рассылает сообщения по рассылкам у которых дата начала раньше
        сегодня и статус запущена всем клиентам рассылки"""

    zone = pytz.timezone('Europe/Moscow')
    current_datetime = datetime.now(zone)

    mail_from = settings.EMAIL_HOST_USER

    # создание объекта с применением фильтра
    # выбираем все со статусом запущена
    mailings = (Sending.objects.filter(start_time__lte=current_datetime)
                               .filter(status__in=['st',]))

    print('Проверка выбора рассылок и клиентов')
    print()
    for mailing in mailings:
        print(f'Активная рассылка: {mailing}')
        print(f'Клиенты по этой рассылке {[client.email for client in mailing.client.all()]}')
        print()

        # устанавливаю для тестов в кроне буду проверять каждую минуту
        time_period = timedelta(minutes=5)

        # Этот блок раскомментировать для работы по расписанию из базы
        # time_period = timedelta(weeks=4)
        # if mailing.period == '1D':
        #     time_period = timedelta(days=1)
        # elif mailing.period == '1W':
        #     time_period = timedelta(weeks=1)

        # принты для проверки
        print(f'Периодичность рассылки {time_period} -> {mailing.period}')
        print(f'Текущее время {current_datetime.strftime(MY_TIME_FORMAT)}')
        print(f'Время последней хорошей рассылки {mailing.last_ok_time.strftime(MY_TIME_FORMAT)}')
        print(mailing.last_ok_time + time_period, '  ', current_datetime)

        # проверка периодичности и рассылка писем
        if mailing.last_ok_time + time_period < current_datetime:
            print('Пора выполнить рассылку')
            mailing.last_ok_time = current_datetime
            mailing.save()
            try:
                server_resp = send_mail(
                    subject=mailing.name,
                    message=mailing.message.body,
                    from_email=mail_from,
                    recipient_list=[client.email for client in mailing.client.all()],
                    fail_silently=False
                )
                MailingAttempt.objects.create(
                    sending=mailing,
                    latest_att_time=current_datetime,
                    status=True,
                    server_response=server_resp
                )
            except smtplib.SMTPException as e:
                MailingAttempt.objects.create(
                    sending=mailing,
                    latest_att_time=current_datetime,
                    status=False,
                    server_response=e.__doc__
                )
