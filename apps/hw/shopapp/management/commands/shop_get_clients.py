from django.core.management.base import BaseCommand
from apps.hw.shopapp.models import ClientModel


class Command(BaseCommand):
    help = "Print existing Client objects with id"

    def handle(self, *args, **options):
        for client in ClientModel.objects.all():
            self.stdout.write(f"{client.id}. {client}")
