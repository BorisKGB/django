from django.core.management.base import BaseCommand
from apps.lections.l2.l2app.models import User


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **options):
        user = User(name='John3', email='some3@mail.addr', password='secret', age=25)  # create new user obj
        user.save()  # add it to SQL
        self.stdout.write(f'{user}')
