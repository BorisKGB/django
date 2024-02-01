from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from apps.seminars.s2.s2Forumapp.models import ArticleModel, AuthorModel
from random import choice


class Command(BaseCommand):
    help = "Create author"

    def handle(self, *args, **options):
        authors = AuthorModel.objects.all()
        for i in range(0, 5):
            article = ArticleModel(title=lorem_ipsum.words(5),
                                   content='\n'.join(lorem_ipsum.paragraphs(4)),
                                   author=choice(authors),  # pick random author
                                   category=lorem_ipsum.words(2))
            article.save()
            self.stdout.write(f'{article}')
