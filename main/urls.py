from django.urls import path
from main import views
from main.views import ClientDetailView, ClientListView

urlpatterns = [
    path('one_client/<int:pk>', ClientDetailView.as_view(), name='one_client'),
    path('all_clients/', ClientListView.as_view(), name='all_clients'),
]
