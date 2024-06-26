from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is First app page")
def courses(request):
    return HttpResponse("This is First app/course page")
def about(request):
    return HttpResponse("This is First app/about page")

