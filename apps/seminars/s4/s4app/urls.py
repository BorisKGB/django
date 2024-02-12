from django.urls import path
from .views import user_action, new_author, new_article


urlpatterns = [
    path('action', user_action, name='user_action'),
    path('new_author', new_author, name='new_author'),
    path('new_article', new_article, name='new_article'),
]
