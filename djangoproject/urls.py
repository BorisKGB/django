"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lections/l1/', include('apps.lections.l1.l1app.urls')),
    path('lections/l3/', include('apps.lections.l3.l3app.urls')),
    path('seminars/s1/', include('apps.seminars.s1.s1app.urls')),
    path('seminars/s3/', include('apps.seminars.s3.s3app.urls')),
    path('hw/hw1/', include('apps.hw.hw1app.urls'))
]
