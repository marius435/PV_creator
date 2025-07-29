from django import forms
from .models import ObjectTypes

class NewObjectType(forms.Form):
    objectName = forms.CharField(
        label='Nume obiect',
        widget=forms.Textarea(),
        max_length=25
    )