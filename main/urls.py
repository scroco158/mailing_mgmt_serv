from django.urls import path
from main import views
from main.views import ClientDetailView, ClientListView, ClientCreateView

urlpatterns = [
    path('one_client/<int:pk>', ClientDetailView.as_view(), name='one_client'),
    path('', ClientListView.as_view(), name='all_clients'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
]
