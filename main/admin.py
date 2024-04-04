from django.contrib import admin
from main.models import Message, Period, Sending, Client


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'body')


@admin.register(Period)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'minutes', 'hours', 'days', 'weeks')


@admin.register(Client)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')


@admin.register(Sending)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'period', 'message', 'status', 'attempt')

