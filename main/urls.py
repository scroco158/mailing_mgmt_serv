from django.urls import path
from main import views
from main.views import ClientDetailView

urlpatterns = [
    path('one_client/<int:pk>', ClientDetailView.as_view(), name='one_client'),
]
