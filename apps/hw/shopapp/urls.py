from django.urls import path
from .views import client_orders, ClientProductsReport


urlpatterns = [
    path('client/<int:client_id>/orders/', client_orders, name='client_orders'),
    path('client/<int:client_id>/product_report/', ClientProductsReport.as_view(), name='product_report'),
    path('client/<int:client_id>/product_report/<str:range>', ClientProductsReport.as_view(), name='product_report'),
]
