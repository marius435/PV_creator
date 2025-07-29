from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Locations, Departaments, Assets, ObjectTypes
from .forms import NewObjectType

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

def inventar(request):
    context = {'current_page': 'inventar',
               'location': Locations,
               'departament': Departaments,
               'newObjectType': ObjectTypes,}
    
    # if request.method == 'POST':

    #     location_name = request.POST['location_name']

    #     add_location = Locations.objects.create(
    #         name=location_name
    #     )


    # if request.method == 'POST':

    #     departament_name = request.POST['departament_name']
    #     locatie_id = int(request.POST['locatie_id'])

    #     location_obj = location.objects.get(pk=locatie_id)

    #     add_departament = departament.objects.create(
    #         departament_name=departament_name,
    #         id_locatie = location_obj

    #     )

    if request.method == 'POST':
        form = NewObjectType(request.POST)
        if form.is_valid():
            name = form.cleaned_data['objectName']
            addObject = ObjectTypes.objects.create(
                name = name,
            )
    else:
        form = NewObjectType()

    return render(request, 'inventar.html', {'context':context, 'form':form})

# from django.shortcuts import render

# # Create your views here.
