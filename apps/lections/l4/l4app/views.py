import logging
from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, ImageForm
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f"We get {name=}, {email=}, {age=}.")
        # else: (doesn't make sense, do this anyway at final return)
        #     if POST and form is invalid rerender form page, but keep correct fields
        #     return render(request, 'l4app/user_form.html', context={'form': form})
    else:
        form = UserForm()
    return render(request, 'l4app/user_form.html', context={'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            logger.info(f"We get {form.cleaned_data=}.")
    else:
        form = ManyFieldsForm()
    return render(request, 'l4app/many_fields_form.html', context={'form': form})


def image_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f"File {image.name} saved.")
    else:
        form = ImageForm()
    return render(request, 'l4app/upload_image.html', context={'form': form})