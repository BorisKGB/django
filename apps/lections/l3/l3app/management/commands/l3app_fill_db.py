from random import choices

from django.core.management.base import BaseCommand
from apps.lections.l3.l3app.models import Author, Post
from django.utils import lorem_ipsum

LOREM = lorem_ipsum.words(50)


class Command(BaseCommand):
    help = "Generate fake authors and posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='records count')

    def handle(self, *args, **options):
        text = LOREM.split()
        count = options.get('count')
        for i in range(1, count + 1):
            author = Author(name=f"Author_{i}", email=f"mail{i}@mamil.ru")
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f"Title-{j}",
                    content=" ".join(choices(text, k=64)),
                    author=author
                )
                post.save()
