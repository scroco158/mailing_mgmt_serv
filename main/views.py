from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from main.models import Client, Message, Sending


# контроллеры по работе с клиентом

class ClientDetailView(DetailView):
    model = Client


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'surname', 'email']
    success_url = reverse_lazy('all_clients')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'surname', 'email']
    success_url = reverse_lazy('all_clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('all_clients')





























# контроллеры по работе с сообщениями

class MessageDetailView(DetailView):
    model = Message

class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ['name', 'body']
    success_url = reverse_lazy('all_messages')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['name', 'body']
    success_url = reverse_lazy('all_messages')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('all_messages')
