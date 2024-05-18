from django.forms import ModelForm

from main.models import Sending


class SendingForm(ModelForm):
    """ Форма для владельца рассылки"""
    class Meta:
        model = Sending
        fields = '__all__'


class ManagerSendingForm(ModelForm):
    """ Форма для группы managers"""
    class Meta:
        model = Sending
        fields = ['status',]