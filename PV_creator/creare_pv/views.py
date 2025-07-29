from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Locations, Departaments, Assets
# from .forms import NewObjectType

def home(request):
    context = {'current_page': 'home'}
    return render(request, 'home.html', context)

def pv_creator(request):
    # tickets = Ticket.objects.all()
    # test = Ticket.objects.all().count()

    test_inv = Assets.objects.all()
    context = { 'current_page': 'pv_creator',
                'db_inventar' : test_inv
                # 'tickets':tickets,
                # 'test':test
                }
    return render(request, 'pv_creator.html', context)

def about(request):
    context = { 'current_page': 'about'}
    return render(request, 'about.html', context)

def inventar(request):
    context = {'current_page': 'inventar',
               'location': Locations,
               'departament': Departaments}
    
    # if request.method == 'POST':

    #     location_name = request.POST['location_name']

    #     add_location = location.objects.create(
    #         location_name=location_name
    #     )


    # if request.method == 'POST':

    #     departament_name = request.POST['departament_name']
    #     locatie_id = int(request.POST['locatie_id'])

    #     location_obj = location.objects.get(pk=locatie_id)

    #     add_departament = departament.objects.create(
    #         departament_name=departament_name,
    #         id_locatie = location_obj

    #     )

    # object = ObjectType

    # if request.method == 'POST':
    #     form = NewObjectType(request.POST)
    #     if form.is_valid():
    #         object_name = form.save(commit=False)
    #         object_name.object_type = object

    #         newObiect = ObjectType.objects.create(
    #             object_type = form.cleaned_data.get('object_name')
    #         )
    #         return redirect('home')
    #     else:
    #         form = NewObjectType()


    # return render(request, 'inventar.html', context)

# from django.shortcuts import render

# # Create your views here.
