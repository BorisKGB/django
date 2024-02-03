from django.core.management.base import BaseCommand, CommandError
from apps.hw.shopapp.models import OrderModel


class Command(BaseCommand):
    help = "Print Order Products by order_id"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='order id')

    def handle(self, *args, **options):
        order_id = options.get('order_id')
        # why .first()?
        order = OrderModel.objects.filter(pk=order_id).first()
        if order:
            for product in order.products.all():
                self.stdout.write(f"{product.id}. {product}")
        else:
            raise CommandError(f"Unable to find Order by id '{order_id}'")
