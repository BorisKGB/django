from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Author, Post


# request represent incoming request object
# this method will answer to any request types (get, post, head,...)
def hello(request):
    return HttpResponse("Hello world from function")


class HelloView(View):
    # answers to get requests
    def get(self, request):
        return HttpResponse("Hello world from class")

    # answers to post requests
    def post(self, request):
        return HttpResponse("Hello world from class")


def year(request, year):
    text = ""
    # some logic
    return HttpResponse(f"you enter {year} - {text}")


class Month(View):
    def get(self, request, year, month):
        text = ""
        # some logic
        return HttpResponse(f"you enter {month}/{year} - {text}")


def detail(request, year, month, slug):
    post = {
        'year': year,
        'month': month,
        'slug': slug
    }
    return JsonResponse(post,
                        json_dumps_params={'ensure_ascii': False})  # allow encodings other than ascii


def my_view(request):
    context = {"name": "user"}
    # I can use apps/hw/hw1app/templates/base.html here by name of "base.html"
    return render(request, "l3app/sample_template.html", context)


class TemplIf(TemplateView):
    template_name = "l3app/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Hello world"
        context['number'] = 5
        return context


def author_posts(request, author_id):
    # get data from sql
    author = get_object_or_404(Author, pk=author_id)  # auto return 404 if no object
    posts = Post.objects.filter(author=author).order_by('-id')[:5]  # last 5 authors
    # and even use them in templates
    return render(request, 'l3app/author_posts.html', context={'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'l3app/post_full.html', context={'post': post})
