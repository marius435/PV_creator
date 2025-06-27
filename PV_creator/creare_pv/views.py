from django.http import HttpResponse
from django.shortcuts import render
from .models import Ticket

def home(request):
    ticket = Ticket.objects.all()
    return render(request, 'home.html', {'tickets': ticket})

def pv_creator(request):
    return render(request, 'pv_creator.html')

def about(request):
    return render(request, 'about.html')

# from django.shortcuts import render

# # Create your views here.
