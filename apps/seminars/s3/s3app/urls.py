from django.urls import path
from .views import CoinAction, DiceAction, RNumAction, author_articles, article


urlpatterns = [
    path('coin/<int:number>', CoinAction.as_view(), name='coin'),
    path('coin/', CoinAction.as_view(), name='coin'),
    path('dice/', DiceAction.as_view(), name='dice'),
    path('dice/<int:number>', DiceAction.as_view(), name='dice'),
    path('rand/', RNumAction.as_view(), name='rand'),
    path('rand/<int:number>', RNumAction.as_view(), name='rand'),
    path('articles/<int:author_id>', author_articles, name='articles'),
    path('article/<int:article_id>', article, name='article'),
]
