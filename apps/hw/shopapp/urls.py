from django.urls import path
from .views import client_orders


urlpatterns = [
    path('client/<int:client_id>/orders/', client_orders, name='client_orders'),
]
