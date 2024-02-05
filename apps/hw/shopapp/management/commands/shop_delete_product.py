from django.core.management.base import BaseCommand, CommandError
from apps.hw.shopapp.models import ProductModel


class Command(BaseCommand):
    help = "Delete Product by id"

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='id')

    def handle(self, *args, **options):
        product_id = options.get('product_id')
        product = ProductModel.objects.filter(pk=product_id).first()
        if product:
            product.deleted = True
            product.save()
        else:
            self.stdout.write("Nothing to do, product not found")
