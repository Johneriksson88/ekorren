from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return render(request, 'index.html')


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")


def user_panel(request):
    return render(request, 'user_panel.html')
