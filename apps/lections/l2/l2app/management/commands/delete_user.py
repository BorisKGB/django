from django.core.management.base import BaseCommand
from apps.lections.l2.l2app.models import User


class Command(BaseCommand):
    help = "Delete user by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **options):
        pk = options['pk']
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')
