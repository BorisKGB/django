from django.core.management.base import BaseCommand
from apps.lections.l2.l2app.models import User


class Command(BaseCommand):
    help = "Get user by id"

    def add_arguments(self, parser):
        # parser.add_argument('id', type=int, help='User ID')
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **options):
        # id = options['id']
        # user = User.objects.get(id=id)  # will raise on nonexistent data
        pk = options['pk']  # for primary key
        user = User.objects.filter(pk=pk).first()  # find by search by primary key and get first
        # on no data we got None
        self.stdout.write(f'{user}')
