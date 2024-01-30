from django.urls import path
from . import views

"""
# Задание 4
Создайте представление “Привет, мир!” внутри вашего первого приложения.
Настройте маршруты
"""


urlpatterns = [
    path('', views.index, name='index'),
    path('index2', views.IndexPageView.as_view(), name='index2'),
    path('coin', views.coin_flip, name='coin_flip'),
    path('dice', views.dice_side, name='dice_side'),
    path('number', views.rand_number, name='rand_number'),
]
