from django.core.management.base import BaseCommand, CommandError
from apps.hw.shopapp.models import OrderModel


class Command(BaseCommand):
    help = "Delete Order by id"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='id')

    def handle(self, *args, **options):
        order_id = options.get('order_id')
        order = OrderModel.objects.filter(pk=order_id).first()
        if order:
            if order.applied_date:
                raise CommandError(f"Not deleting closed orders")
            order.delete()
        else:
            self.stdout.write("Nothing to do, order not found")
