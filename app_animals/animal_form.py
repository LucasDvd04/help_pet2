from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        placeholders = {
            'name': 'Enter animal name',
            'age': 'Enter animal age',
        }


class FilterForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['gender','specie','status','state','age']
        
        
