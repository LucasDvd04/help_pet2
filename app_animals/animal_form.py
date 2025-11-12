from django import forms
from .models import Animal, PictureGalery

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

        labels = {
            'name':'Nome',
            'age': 'Idade',
            'gender': 'Genero',
            'specie': 'Especie',
            'status': 'Situação',
            'description': 'Descrição'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Ex: Caramelo','required':'True'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Ex: 5'}),
            'description': forms.Textarea(attrs={'placeholder': 'Ex: Animal docil e muito amoroso, tem uma marca de nacença....', 'rows':3})
        }


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class GaleryForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=MultipleFileInput(attrs={'multiple': True}),
        label="Selecione até 3 fotos",
        required=True
    )

    class Meta:
        model = PictureGalery
        fields = ['picture']


        
        
