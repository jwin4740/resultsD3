from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1> results page </h1>")


def responseNumber(request, task_id):
    print(task_id)
    return HttpResponse("<h1> results page with numbers</h1>")
