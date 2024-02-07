from django.views.generic import TemplateView
from .models import ClientModel, ProductModel, OrderModel
from django.http import HttpResponse
from django.shortcuts import render


def client_orders(request: HttpResponse, client_id: int):
    # client = get_object_or_404(ClientModel, pk=client_id)
    orders = OrderModel.objects.filter(client__id=client_id)
    return render(request, 'shopapp/client_orders.html',
                  context={'orders': orders, 'client_id': client_id})
