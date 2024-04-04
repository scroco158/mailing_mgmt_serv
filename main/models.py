from django.db import models


class Message(models.Model):
    """ Сообщение для рассылки"""
    name = models.CharField(max_length=50, verbose_name='тема сообщения для рассылки')
    body = models.TextField(verbose_name='текст сообщения для рассылки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'сообщение для рассылки'
        verbose_name_plural = 'сообщения для рассылки'
        ordering = ('name',)


class Period(models.Model):
    """ Периодичность рассылки """
    name = models.CharField(max_length=50, verbose_name='периодичность рассылки сообщения')
    minutes = models.IntegerField(default=0, verbose_name='минуты')
    hours = models.IntegerField(default=0, verbose_name='часы')
    days = models.IntegerField(default=0, verbose_name='дни')
    weeks = models.IntegerField(default=0, verbose_name='недели')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'периодичность'
        verbose_name_plural = 'периодичности'


class MailingAttempt(models.Model):
    """ Попытка рассылки """
    latest_att_time = models.DateTimeField(verbose_name='время последней попытки')
    status = models.BooleanField(default=False, verbose_name='статус')
    server_response = models.TextField(verbose_name='ответ сервера')


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    email = models.EmailField(verbose_name='почта')

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
    name = models.CharField(max_length=50, verbose_name='название рассылки')
    start_time = models.DateTimeField(verbose_name='время начала')
    end_time = models.DateTimeField(verbose_name='время завершения', null=True, blank=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, verbose_name='периодичность рассылки')
    client = models.ManyToManyField(Client, verbose_name='клиент')
    message = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name='содержание рассылки')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='cr')
    attempt = models.ForeignKey(MailingAttempt, on_delete=models.CASCADE,verbose_name='попытка рассылки', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
