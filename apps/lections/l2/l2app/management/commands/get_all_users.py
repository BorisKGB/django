from django.core.management.base import BaseCommand
from apps.lections.l2.l2app.models import User


class Command(BaseCommand):
    help = "Get all users"

    def handle(self, *args, **options):
        users = User.objects.all()  # objects allow access to SQL data
        self.stdout.write(f'{users}')
