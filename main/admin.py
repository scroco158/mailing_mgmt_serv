from django.contrib import admin
from main.models import Message, Sending, Client, MailingAttempt


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'body')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname', 'email')


@admin.register(Sending)
class SendingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'start_time', 'end_time', 'period', 'status', 'message', 'last_ok_time')


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sending', 'latest_att_time', 'status', 'server_response')
