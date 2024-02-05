from django.urls import path
from .views import HelloView, hello, year, Month, detail, my_view, TemplIf
from .views import author_posts, post_full

urlpatterns = [
    # '/' at the end will auto 301 user when access addr without '/' at the end
    path('hello_m/', hello, name='hello_m'),
    path('hello_c', HelloView.as_view(), name='hello_c'),
    path('<int:year>/', year, name='year'),
    path('<int:year>/<int:month>/', Month.as_view(), name='month'),
    # slug is special type
    path('<int:year>/<int:month>/<slug:slug>/', detail, name='detail'),
    path('template', my_view, name='template'),
    path('tmp_if', TemplIf.as_view(), name='tmp_if'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),
]
