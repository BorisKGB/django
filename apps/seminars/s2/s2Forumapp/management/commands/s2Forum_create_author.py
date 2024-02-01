from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from apps.seminars.s2.s2Forumapp.models import AuthorModel


class Command(BaseCommand):
    help = "Create author"

    def handle(self, *args, **options):
        for i in range(0, 5):
            author = AuthorModel(name=f"Author_{i}",
                                 surname=f"Surname_{i}",
                                 email='some3@mail.addr',
                                 biography=lorem_ipsum.words(10),
                                 birthday='1900-11-12')
            author.save()
            self.stdout.write(f'{author}')
