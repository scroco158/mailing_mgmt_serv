from django.core.mail import send_mail
from config import settings


def send_information_mail(post_name):

    email_from = settings.EMAIL_HOST_USER
    # print(email_from)
    # print(settings.EMAIL_HOST_USER)
    # print(settings.EMAIL_HOST_PASSWORD)

    send_mail(
        '100 просмотров',
        f'Поздравляю ваш пост {post_name} просмотрели 100 раз',
        email_from,
        ('scroco@mail.ru',)
    )
