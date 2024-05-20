from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView

from config.settings import EMAIL_HOST_USER
from users.forms import UserCreationForm
from users.models import User

import secrets
from django.core.mail import send_mail


class UserListView(ListView):
    model = User


class UserCreateView(CreateView):
    """ Создание пользователя """
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ Верификация почты пользователя"""

        user = form.save()             # сохранение данные из формы
        token = secrets.token_hex(16)  # генерация токена
        user.is_active = False         # устанавливаем пользователя не активным
        user.token = token             # устанавливаем пользователю токен
        user.save()                    # сохраняем пользователя

        # формирую ссылку для отправки пользователю
        host = self.request.get_host()                      # получаю адрес хоста
        url = f'http://{host}/users/confirm_email/{token}'  # ссылка для отправки

        # отправка письма
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейдите по ссылке для подтверждения {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email,]
        )
        return super().form_valid(form)


def mail_verification(request, token):
    """ Обработка перехода пользователя по отправленной ссылке"""
    user = get_object_or_404(User, token=token)  # ищем пользователя по токену
    user.is_active = True                        # если найден - то активируем
    user.save()                                  # сохраняем
    return redirect(reverse('users:login'))      # редиректим на вход


def user_status_change(request, pk):

    one_user = get_object_or_404(User, pk=pk)
    if one_user.is_active:
        one_user.is_active = False
    else:
        one_user.is_active = True
    one_user.save()
    return redirect(reverse('users:all_users'))



