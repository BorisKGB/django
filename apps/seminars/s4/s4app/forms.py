from django.forms import Form, ChoiceField, RadioSelect, IntegerField
from django.forms import ModelForm
from apps.seminars.s3.s3app.models import AuthorModel, ArticleModel


class ActionForm(Form):
    action = ChoiceField(choices=[('coin', 'Coin flip'), ('dice', 'Dice side'), ('rand', 'Random number')],
                         widget=RadioSelect())
    attempts = IntegerField(min_value=1, max_value=64)


# create form from model definition
class NewAuthorForm(ModelForm):
    class Meta:
        model = AuthorModel
        exclude = ['fullname']  # use all fields except
        # fields = ['name', 'surname', 'email', 'biography', 'birthday']  # or set field names manually
        # fields = [f.name for f in AuthorModel._meta.get_fields()]  # not work, https://docs.djangoproject.com/en/5.0/ref/models/meta/


class NewArticle(ModelForm):
    # ArticleModel.author = models.ForeignKey will auto populate itself to choice list in form
    class Meta:
        model = ArticleModel
        exclude = ['views_count']
