from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.


def index(request):
    return render(request, "portfolio_app/index.html")


def section_two(request):
    return render(request, "portfolio_app/sectiontwo.html")
