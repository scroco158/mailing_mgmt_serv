from django.shortcuts import render
from django.views.generic import DetailView, ListView

from main.models import Client


class ClientDetailView(DetailView):
    model = Client


class ClientListView(ListView):
    model = Client


