from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *


def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.all():  # минус потом, что по убыванию
        s += str(bb.title) + '\n' + str(bb.content) + '\n' + str(bb.published) + '\n\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')


def index1(request):
    bbs = Bb.objects.order_by('-published')
    rs = Rubric.objects.all()
    return render(request, "btest/index.html", {'bbs': bbs, 'rs' : rs})
