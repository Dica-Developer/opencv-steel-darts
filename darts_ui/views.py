from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from django.views import generic

from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'darts_ui/index.html', {})
