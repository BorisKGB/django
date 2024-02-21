from django.urls import path
from .views import client_orders, ClientProductsReport, product_info, new_product
from .admin import shop_admin


urlpatterns = [
    path('client/<int:client_id>/orders/', client_orders, name='client_orders'),
    path('client/<int:client_id>/product_report/', ClientProductsReport.as_view(), name='product_report'),
    path('client/<int:client_id>/product_report/<str:range>', ClientProductsReport.as_view(), name='product_report'),
    path('product/<int:product_id>/', product_info, name='product_info'),
    path('product/new/', new_product, name='new_product'),
    path('admin/', shop_admin.urls)
]
