from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Locations, Departaments, Assets, ObjectTypes
from .forms import NewObjectType
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    context = {'current_page': 'home'}
    return render(request, 'home.html', context)

def pv_creator(request):
    test_inv = Assets.objects.all()
    context = { 'current_page': 'pv_creator',
                'db_inventar' : test_inv,
                }
    return render(request, 'pv_creator.html', context)

def about(request):
    context = { 'current_page': 'about'}
    return render(request, 'about.html', context)




def objectTypes(request):
    context = {'current_page': 'inventar',
               'curentTablePAge': 'objectTypes'}
    
    object_list = ObjectTypes.objects.all()
    paginator = Paginator(object_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj
    return render(request, 'objectTypes.html', context)


def departaments(request):
    context = {'current_page': 'inventar',
               'curentTablePage': 'departaments'}
    
    object_list = Departaments.objects.all()
    paginator = Paginator(object_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj
    return render(request, 'departaments.html', context)


def inventar(request):
    context = {'current_page': 'inventar',   
               'newObjectType': ObjectTypes,}

    if request.method == 'POST':
        form = NewObjectType(request.POST)
        if form.is_valid():
            name = form.cleaned_data['objectName']
            addObject = ObjectTypes.objects.create(
                name = name,
            )
        context['currentTable'] = 'ObjectTypes'
    else:
        form = NewObjectType()

    context['form']= form

    return render(request, 'inventar.html', context)