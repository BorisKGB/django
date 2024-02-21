from django.shortcuts import render, redirect, reverse
from .forms import ActionForm, NewAuthorForm, NewArticle
from apps.seminars.s3.s3app.views import CoinAction, DiceAction, RNumAction


def user_action(request):
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            attempts = form.cleaned_data['attempts']
            if form.cleaned_data.get('action') == 'coin':
                # redirect to view from s3app by url name with parameters
                # return redirect(reverse('coin', args=[attempts]))
                return redirect('coin', number=attempts)
            elif form.cleaned_data.get('action') == 'dice':
                # unable to correctly modify request on the go
                # # probably should not do that, without this i get 405 method not allowed
                request.method = 'GET'
                # request.path = '5'
                # from django.urls.resolvers import ResolverMatch
                # request.resolver_match = ResolverMatch(func=None, args=[], kwargs={'number': 5})
                # request.resolver_match.captured_kwargs = {'number': 5}
                # request.resolver_match.route = '<int:number>'
                # # lost attempts data on that part,
                return DiceAction.as_view()(request)
                # return redirect(reverse('dice', args=[attempts]))
            elif form.cleaned_data.get('action') == 'rand':
                return redirect(reverse('rand', args=[attempts]))
            # if i create views as methods i probably was able to do:
            # else:
            #   return view_method(request, **params)
    else:
        form = ActionForm()
    return render(request, 'l4app/user_form.html', context={'form': form})


def new_author(request):
    if request.method == 'POST':
        form = NewAuthorForm(request.POST)
        if form.is_valid():  # when ModelForm valid it already contains ready to commit Model obj
            new_author_obj = form.save()  # just add record to SQL
            # redirect to author page on creation
            return redirect(reverse('articles', args=[new_author_obj.pk]))
            # alternate you can create Model objects using Model.objects.create(key=val,...)
            # by creating them this way values will automatically be validated accordingly to Model limits
    else:
        form = NewAuthorForm()
    return render(request, 'l4app/user_form.html', context={'form': form})


def new_article(request):
    if request.method == 'POST':
        form = NewArticle(request.POST)
        if form.is_valid():
            new_article_obj = form.save()
            return redirect(reverse('article', args=[new_article_obj.pk]))
    else:
        form = NewArticle()
    return render(request, 'l4app/user_form.html', context={'form': form})
