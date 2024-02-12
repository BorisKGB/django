from django.forms import ModelForm
from .models import ProductModel


class NewProductForm(ModelForm):

    class Meta:
        model = ProductModel
        exclude = ['deleted']  # 'created' will be excluded automatically via 'auto_now_add'
