from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return render(request, "app_main/index.html")


def form (request):
    return render(request, "app_main/form.html")