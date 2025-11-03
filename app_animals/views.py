from django.shortcuts import render
from django.http import HttpResponse
from .animal_form import AnimalForm, FilterForm
from .models import Animal

# Create your views here.

def home_screen(request):
    return render(request, 'home.html')

def animal_cad_screen(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Animal cadastrado com sucesso!")
    form = AnimalForm()
    return render(request, 'animals_cad.html', {'form': form})

def animal_list_screen(request):
    animais = Animal.objects.filter(status__status='Desaparecido')
    form = FilterForm()
    return render(request, 'animals_list.html', {'animais': animais, 'form': form})

def animal_list_screen_filt(request):
    filters = request.GET.get('gender')
    print(filters)
    animais = Animal.objects.filter(status__status='Desaparecido')
    form = FilterForm()
    return render(request, 'animals_list.html', {'animais': animais, 'form': form})