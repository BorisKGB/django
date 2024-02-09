from django.urls import path
from .views import user_form, many_fields_form, image_form


urlpatterns = [
    path('form', user_form, name='user_form'),
    path('many_form', many_fields_form, name='many_fields_form'),
    path('image', image_form, name='image_form'),
]
