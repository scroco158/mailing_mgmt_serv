from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import (ClientDetailView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView,
                        MessageDetailView, MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView,
                        SendingListView, SendingDetailView, SendingCreateView, SendingUpdateView, SendingDeleteView,
                        run_by_button, turn_on_schedule, turn_off_schedule, front_page, MailingAttemptListView)

urlpatterns = [

    path('', front_page, name='front_page'),
    path('all_mailingattempt', MailingAttemptListView.as_view(), name='all_mailingattempt'),

    path('one_client/<int:pk>', ClientDetailView.as_view(), name='one_client'),
    path('all_clients', ClientListView.as_view(), name='all_clients'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    path('one_message/<int:pk>', MessageDetailView.as_view(), name='one_message'),
    path('all_messages/', MessageListView.as_view(), name='all_messages'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('update_message/<int:pk>', MessageUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),

    path('one_sending/<int:pk>', cache_page(60)(SendingDetailView.as_view()), name='one_sending'),
    path('all_sendings/', SendingListView.as_view(), name='all_sendings'),
    path('create_sending/', SendingCreateView.as_view(), name='create_sending'),
    path('update_sending/<int:pk>', SendingUpdateView.as_view(), name='update_sending'),
    path('delete_sending/<int:pk>', SendingDeleteView.as_view(), name='delete_sending'),

    path('run_by_button/', run_by_button, name='run_by_button'),
    path('turn_on_schedule/', turn_on_schedule, name='turn_on_schedule'),
    path('turn_off_schedule/', turn_off_schedule, name='turn_off_schedule')

]
