from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Home page')

def about(request):
    return HttpResponse('About page')

def contact(request):
    return HttpResponse('Contact page')

def products(request):
    return HttpResponse('Products page')

def customer(request):
    return HttpResponse('Customer page')
