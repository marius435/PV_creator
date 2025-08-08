from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Locations, Departaments, Assets, ObjectTypes, Locations
from .forms import AddObjectType, AddLocation, AddDepartament
from django.views.generic import ListView, View, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy

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


class addLocation(CreateView):
    model = Locations
    form_class = AddLocation 
    template_name = 'addLocation.html'
    success_url = reverse_lazy('assets') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'assets'
        return context
    
class addDepartament(CreateView):
    model = Departaments
    form_class = AddDepartament
    template_name = 'addLocation.html'
    success_url = reverse_lazy('assets') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'assets'
        return context

class addObjectType(CreateView):
    model = ObjectTypes
    form_class = AddObjectType
    template_name = 'addLocation.html'
    success_url = reverse_lazy('assets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'assets'
        return context



def locations(request):
    context = {'current_page': 'assets',
               'currentTablePage': 'locations'}
    
    objectList = Locations.objects.all()
    paginator = Paginator(objectList, 5)

    pageNumber = request.GET.get("page")
    pageObj = paginator.get_page(pageNumber)

    context['pageObj'] = pageObj
    return render(request, 'locations.html', context)

def departaments(request):
    context = {'current_page': 'assets',
               'currentTablePage': 'departaments'}
    
    object_list = Departaments.objects.all()
    paginator = Paginator(object_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj
    return render(request, 'departaments.html', context)

def objectTypes(request):
    context = {'current_page': 'assets',
               'currentTablePAge': 'objectTypes'}
    
    object_list = ObjectTypes.objects.all()
    paginator = Paginator(object_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj
    return render(request, 'objectTypes.html', context)



def assets(request):
    context = {'current_page': 'assets',   
               'newObjectType': ObjectTypes,}

    if request.method == 'POST':
        form = AddObjectType(request.POST)
        if form.is_valid():
            name = form.cleaned_data['objectName']
            addObject = ObjectTypes.objects.create(
                name = name,
            )
        context['currentTable'] = 'ObjectTypes'
    else:
        form = AddObjectType()

    context['form']= form

    return render(request, 'assets.html', context)