from django.http import HttpResponse
from django.shortcuts import render
from .models import Ticket

def home(request):
    context = {'current_page': 'home'}
    return render(request, 'home.html', context)

def pv_creator(request):
    context = { 'current_page': 'pv_creator'}
    return render(request, 'pv_creator.html', context)

def about(request):
    context = { 'current_page': 'about'}
    return render(request, 'about.html', context)


# from django.shortcuts import render

# # Create your views here.
