from django.core.management.base import BaseCommand
from apps.hw.shopapp.models import OrderModel


class Command(BaseCommand):
    help = "Print existing Order objects with id"

    def handle(self, *args, **options):
        for order in OrderModel.objects.all():
            self.stdout.write(f"{order.id}. {order}")
