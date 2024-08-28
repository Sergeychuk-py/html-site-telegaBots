from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import HttpResponse

from app_main.forms import MyForms


def index(request):
    return render(request, "app_main/index.html")


def form(request):
    if request.method == "POST":
        form = MyForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request submitted successfully.')
            return render(request, 'app_main/messages.html', {'form': MyForms(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = MyForms()
    return render(request, "app_main/form.html", {'form': form})