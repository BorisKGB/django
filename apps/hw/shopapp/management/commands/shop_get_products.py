from django.core.management.base import BaseCommand
from apps.hw.shopapp.models import ProductModel


class Command(BaseCommand):
    help = "Print existing Product objects with id"

    def handle(self, *args, **options):
        for product in ProductModel.objects.all():
            self.stdout.write(f"{product.id}. {product}")
