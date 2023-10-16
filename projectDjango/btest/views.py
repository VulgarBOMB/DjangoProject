from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *


def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):  # минус потом, что по убыванию
        s += str(bb.title) + '\r\n' + str(bb.content) + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')


def index1(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, "btest/index.html", {'bbs': bbs})
