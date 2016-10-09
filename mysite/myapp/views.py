from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def result(request, page_number):
    return HttpResponse("Page " + page_number)
