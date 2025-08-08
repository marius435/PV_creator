from django import forms
from .models import Assets, Locations, Departaments, DepartmentObjects, ObjectTypes, InventoryClasses, Persons



class AddLocation(forms.ModelForm):
    class Meta:
        model = Locations

        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume locatie'}),}
        
class AddDepartament(forms.ModelForm):
    
    class Meta:
        model = Departaments

        fields = ['name', 'location']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume departament'}),
            }

class AddObjectType(forms.ModelForm):
    
    class Meta:
        model = ObjectTypes

        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume obiect'}),
            }
        