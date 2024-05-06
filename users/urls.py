from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .apps import UsersConfig
from .views import UserCreateView, mail_verification

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('confirm_email/<str:token>/', mail_verification, name='mail_verification'),
]
