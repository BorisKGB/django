from django.core.management.base import BaseCommand
from apps.lections.l2.l2app.models import User


class Command(BaseCommand):
    help = "Update user name by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='New user name')

    def handle(self, *args, **options):
        pk = options['pk']
        new_name = options['name']
        user = User.objects.filter(pk=pk).first()
        user.name = new_name
        user.save()
        self.stdout.write(f'{user}')
