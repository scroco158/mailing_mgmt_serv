from django.urls import path
from main import views
from main.views import (ClientDetailView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView,
                        MessageDetailView, MessageListView)

urlpatterns = [

    path('one_client/<int:pk>', ClientDetailView.as_view(), name='one_client'),
    path('', ClientListView.as_view(), name='all_clients'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    path('one_message/<int:pk>', MessageDetailView.as_view(), name='one_message'),
    path('all_messages/', MessageListView.as_view(), name='all_messages'),

]
