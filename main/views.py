from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from main.models import Client, Message, Sending
from main.services import send_mailing
from django.core.management import call_command


# контроллеры по работе с клиентом
class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        cl_queryset = super().get_queryset()
        user = self.request.user
        return cl_queryset.filter(owner=user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['name', 'surname', 'email']
    success_url = reverse_lazy('all_clients')

    def form_valid(self, form):
        cl_form = form.save()
        cl_form.owner = self.request.user
        cl_form.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['name', 'surname', 'email']
    success_url = reverse_lazy('all_clients')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('all_clients')


# контроллеры по работе с сообщениями
class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        mes_queryset=super().get_queryset()
        user = self.request.user
        return mes_queryset.filter(owner=user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['name', 'body']
    success_url = reverse_lazy('all_messages')

    def form_valid(self, form):
        mes_form = form.save()
        user = self.request.user
        mes_form.owner = user
        mes_form.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ['name', 'body']
    success_url = reverse_lazy('all_messages')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('all_messages')


# контроллеры по работе с рассылками
class SendingDetailView(LoginRequiredMixin, DetailView):
    model = Sending


class SendingListView(LoginRequiredMixin, ListView):
    """ Список всех рассылок"""
    model = Sending

    def get_queryset(self):
        """ Фильтр по текущему пользователю"""
        sen = super().get_queryset()
        user = self.request.user
        return sen.filter(owner=user)


class SendingCreateView(LoginRequiredMixin, CreateView):
    model = Sending
    fields = ['name', 'start_time', 'end_time', 'client', 'period', 'status', 'message', 'last_ok_time']
    success_url = reverse_lazy('all_sendings')

    def form_valid(self, form):
        sending = form.save()
        user = self.request.user
        sending.owner = user
        sending.save()
        return super().form_valid(form)


class SendingUpdateView(LoginRequiredMixin, UpdateView):
    model = Sending
    fields = ['name', 'start_time', 'end_time', 'client', 'period', 'status', 'message', 'last_ok_time']
    success_url = reverse_lazy('all_sendings')


class SendingDeleteView(LoginRequiredMixin, DeleteView):
    model = Sending
    success_url = reverse_lazy('all_sendings')


# контроллер для запуска бизнес логики
@login_required
def run_by_button(request):
    """
    Запускает разовую проверку условий необходимости выполнения рассылок
    и при выполнении условий делает рассылку
    """
    send_mailing()
    return redirect(reverse('all_clients'))


@login_required
def turn_on_schedule(request):
    """
    Запускает периодическую проверку условий необходимости выполнения рассылок
    Регулярность проверки выполнения рассылок согласно параметрам в settings.py
    """
    call_command('crontab', 'add')
    return redirect(reverse('all_clients'))


@login_required
def turn_off_schedule(request):
    """
    Выключает периодическую проверку условий необходимости выполнения рассылок
    """
    print('выключение расписания')
    call_command('crontab', 'remove')
    return redirect(reverse('all_clients'))


def front_page(request):
    return render(request, 'main/front_page.html')