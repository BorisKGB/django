from django.views.generic import TemplateView
import random
from .models import ArticleModel, AuthorModel
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404


class ActionTmpl(TemplateView):
    action_name = None
    template_name = f"s3app/base.html"

    def action(self, number: int):
        raise NotImplemented()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'number' not in context:
            context['number'] = 1
        context['action'] = self.action_name
        context['results'] = self.action(context['number'])
        return context


class CoinAction(ActionTmpl):
    action_name = 'Coin flip'

    def action(self, number: int):
        return [random.choice(['head', 'tail']) for _ in range(number)]


class DiceAction(ActionTmpl):
    action_name = 'Dice side'

    def action(self, number: int):
        return [random.choice([1, 2, 3, 4, 5, 6]) for _ in range(number)]


class RNumAction(ActionTmpl):
    action_name = "Random number"

    def action(self, number: int = 1):
        return [random.randint(0, 100) for _ in range(number)]


def author_articles(request: HttpResponse, author_id: int):
    articles = ArticleModel.objects.filter(author__id=author_id)
    return render(request, 's3app/articles.html', context={'articles': articles})


def article(request: HttpResponse, article_id: int):
    article = get_object_or_404(ArticleModel, pk=article_id)
    article.views_count += 1
    article.save()
    return render(request, 's3app/article.html', context={'article': article})
