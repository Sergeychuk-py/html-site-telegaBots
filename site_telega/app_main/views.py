from django.shortcuts import render
from django.shortcuts import HttpResponse
from app_main.forms import NameForm


def index(request):
    return render(request, "app_main/index.html")


def form(request):
    form = NameForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        new_form = form.save()
    return render(request, "app_main/form.html")