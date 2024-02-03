from django.core.management.base import BaseCommand, CommandError
from apps.hw.shopapp.models import ProductModel


class Command(BaseCommand):
    help = "Update Product cost by id"

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='id')
        parser.add_argument('cost', type=float, help='new cost')

    def handle(self, *args, **options):
        product_id = options.get('product_id')
        new_cost = options.get('cost')
        product = ProductModel.objects.filter(pk=product_id).first()
        if product:
            product.cost = new_cost
            product.save()
            # Возможно тут я должен выполнить перерасчёт total_amount для открытых Orders, к обсуждению
        else:
            raise CommandError(f"Unable to find Product by id '{product_id}'")
