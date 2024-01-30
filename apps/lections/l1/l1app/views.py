from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page log")
    return HttpResponse("Hello world")


def about(request):
    logger.debug('some about page debug message')
    return HttpResponse("About us")
