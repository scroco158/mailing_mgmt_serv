from django.db import models


class Message(models.Model):
    """ Сообщение для рассылки"""
    name = models.CharField(max_length=50, verbose_name='тема сообщения')
    body = models.TextField(verbose_name='текст сообщения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Period(models.Model):
    """ Периодичность рассылки """
    name = models.CharField(max_length=50, verbose_name='периодичность')
    hour = models.IntegerField(verbose_name='часы')
    day = models.IntegerField(verbose_name='дни')
    week = models.IntegerField(verbose_name='недели')

    def __str__(self):
        return self.name


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


class Sending(models.Model):
    """ Настройки рассылки"""
    name = models.CharField(max_length=50, verbose_name='название рассылки')
    start_time = models.DateTimeField(verbose_name='время начала')
    end_time = models.DateTimeField(verbose_name='время завершения')
    period = models.ForeignKey(Period, on_delete=models.CASCADE, verbose_name='периодичность рассылки')
    client = models.ManyToManyField(Client, verbose_name='клиент')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='содержание рассылки')
    attempt = models.ForeignKey(MailingAttempt, on_delete=models.CASCADE,verbose_name='попытка рассылки', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


