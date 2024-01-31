from django.shortcuts import render

LINKS = [
    {
        'name': 'Main page',
        'url_for': 'main_page'
    },
    {
        'name': 'About me',
        'url_for': 'about_page'
    }
]


def main_page(request):
    data = {
        'title': 'Main page',
    }
    return render(request, 'base.html', {**data, 'links': LINKS})


def about_page(request):
    data = {
        'title': 'About me',
    }
    return render(request, 'base.html', {**data, 'links': LINKS})