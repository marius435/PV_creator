from django.http import HttpResponse
from django.shortcuts import render
from .models import db_inventar
# from .models import Ticket

def home(request):
    context = {'current_page': 'home'}
    return render(request, 'home.html', context)

def pv_creator(request):
    # tickets = Ticket.objects.all()
    # test = Ticket.objects.all().count()

    test_inv = db_inventar.objects.all()
    context = { 'current_page': 'pv_creator',
                'db_inventar' : test_inv
                # 'tickets':tickets,
                # 'test':test
                }
    return render(request, 'pv_creator.html', context)

def about(request):
    context = { 'current_page': 'about'}
    return render(request, 'about.html', context)


# from django.shortcuts import render

# # Create your views here.
