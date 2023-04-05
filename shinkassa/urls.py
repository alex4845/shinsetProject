from django.urls import path
from .views import index, add, views
urlpatterns = [
    path("", index, name="Главная"),
    path("add", add, name="Добавление записи"),
    path("views", views, name="Просмотр"),
]