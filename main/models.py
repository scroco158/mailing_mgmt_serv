from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    """ Сообщение для рассылки """
    name = models.CharField(max_length=50, verbose_name='тема сообщения для рассылки')
    body = models.TextField(verbose_name='текст сообщения для рассылки')

    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'сообщение для рассылки'
        verbose_name_plural = 'сообщения для рассылки'
        ordering = ('name',)


class Client(models.Model):
    """ Клиент рассылки (получатель) """
    name = models.CharField(max_length=50, verbose_name='имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(default='scroco@mail.ru', verbose_name='почта')

    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Sending(models.Model):
    """ Настройки рассылки"""

    STATUS_CHOICES = [
        ('en', 'Завершена'),
        ('cr', 'Создана'),
        ('st', 'Запущена'),
    ]

    PERIOD_CHOICES = [
        ('1D', 'раз в день'),
        ('1W', 'раз в неделю'),
        ('1M', 'раз в месяц'),
    ]

    name = models.CharField(max_length=50, verbose_name='название рассылки')
    start_time = models.DateTimeField(verbose_name='время начала')
    end_time = models.DateTimeField(verbose_name='время завершения', **NULLABLE)
    period = models.CharField(max_length=2, choices=PERIOD_CHOICES, verbose_name='периодичность рассылки')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='cr')
    client = models.ManyToManyField(Client, verbose_name='клиент')
    message = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name='содержание рассылки')
    last_ok_time = models.DateTimeField(verbose_name='дата последней удачной рассылки', **NULLABLE)

    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('start_time',)

        permissions = [('can_view_all_sendings', 'can view all sendings'),
                       ('can_switch_status', 'can switch status'),
                       ]


class MailingAttempt(models.Model):
    """ Попытка рассылки """

    sending = models.ForeignKey(Sending, on_delete=models.CASCADE, verbose_name='related sending', **NULLABLE)
    latest_att_time = models.DateTimeField(verbose_name='время последней попытки')
    status = models.BooleanField(default=False, verbose_name='статус последней попытки')
    server_response = models.TextField(verbose_name='ответ сервера')

    def __str__(self):
        return self.server_response

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
        ordering = ('latest_att_time',)
