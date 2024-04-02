from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from main.models import Client


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
