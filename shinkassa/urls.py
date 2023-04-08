from django.urls import path
from .views import index, add, views, registration, exit_user, enter_user

urlpatterns = [
    path("", index, name="Главная"),
    path("add", add, name="Добавление записи"),
    path("views", views, name="Просмотр"),
    path("registration", registration, name="Регистрация"),
    path("exit_user", exit_user, name="Выход"),
    path("enter_user", enter_user, name="Вход"),
]