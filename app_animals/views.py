from pyexpat.errors import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from .animal_form import AnimalForm,GaleryForm
from .models import Animal, Location, PictureGalery, Comment
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

def home_screen(request):
    return render(request, 'home.html')

def animal_cad_screen(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        picture_form = GaleryForm(request.POST, request.FILES)
        files = request.FILES.getlist('picture')

        if form.is_valid():
            # ⚠ NÃO salva ainda, para poder adicionar o user
            new_animal = form.save(commit=False)
            new_animal.user = request.user           # <- AQUI o user é preenchido automaticamente
            new_animal.save()                        # salva agora

            # salvar as fotos
            for f in files:
                PictureGalery.objects.create(
                    picture=f,
                    animal=new_animal                # pode usar diretamente
                )

            return HttpResponse("Animal cadastrado com sucesso!")

    # GET request
    form = AnimalForm()
    picture_form = GaleryForm()
    return render(request, 'animals_cad.html', {'form': form, 'pic': picture_form})

class AnimalDelete(generic.DeleteView):
    model  = Animal
    template_name = 'animal_delete.html'
    success_url = reverse_lazy('user_profile')

class AnimaCadView(generic.CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animals_cad.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user  # <- preenche automaticamente
        return super().form_valid(form)
    


def animal_lost_screen(request):

    if request.method == 'GET':
            animais = Animal.objects.filter(status='desaparecido').prefetch_related('picture_animal').order_by('-dt_create')
            
            for animal in animais:
                print(f"Animal: {animal.name}")
                for foto in animal.picture_animal.all():
                    print(f" - Foto: {foto.picture.url}")
                    
            locations = Location.objects.all()
            

    return render(request, 'animals_list.html', {'animais': animais})


def animal_adoction_screen(request):

    if request.method == 'GET':
            animais = Animal.objects.filter(status='adocao').prefetch_related('picture_animal')

            for animal in animais:
                print(f"Animal: {animal.name}")
                for foto in animal.picture_animal.all():
                    print(f" - Foto: {foto.picture.url}")
                    
            locations = Location.objects.all()
            

    return render(request, 'animals_list.html', {'animais': animais})


def animal_abandoned_screen(request):

    if request.method == 'GET':
            # animais = Animal.objects.filter(status='desaparecido').values()
            animais = Animal.objects.filter(status='abandonado').prefetch_related('picture_animal')

            for animal in animais:
                print(f"Animal: {animal.name}")
                for foto in animal.picture_animal.all():
                    print(f" - Foto: {foto.picture.url}")
                    
            locations = Location.objects.all()
            

    return render(request, 'animals_list.html', {'animais': animais})

class AnimalsListView(generic.ListView):
    model = Animal
    template_name = 'animals_list.html'
    context_object_name = 'animais'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        location = self.request.GET.get('location')
        
        if location:
            print(location)
            return queryset.filter(state=location)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        context['pictures'] = PictureGalery.objects.filter(animal='11')
        return context
    

class AnimalLostDetailView(generic.DetailView):   
    model = Animal
    context_object_name = 'animais'
    template_name = 'detail_lost.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_animal.filter(animal=self.object).order_by('dt_create')
        
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        content = request.POST.get('comment')
        comment_edit = request.POST.get('comment_edit')
        comment_id = request.POST.get('comment_id')

     
        if comment_id:
            print(comment_id, comment_edit)
            comentario = get_object_or_404(Comment, id=comment_id)
            comentario.content = comment_edit
            comentario.save()
        else:    
            Comment.objects.create(
                content=content,
                animal=self.object,
                user=request.user
            )

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    

class AnimalAdoctDetailView(generic.DetailView):   
    model = Animal
    context_object_name = 'animais'
    template_name = 'detail_adoct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_animal.filter(animal=self.object).order_by('dt_create')
        
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        content = request.POST.get('comment')
        comment_edit = request.POST.get('comment_edit')
        comment_id = request.POST.get('comment_id')

     
        if comment_id:
            print(comment_id, comment_edit)
            comentario = get_object_or_404(Comment, id=comment_id)
            comentario.content = comment_edit
            comentario.save()
        else:    
            Comment.objects.create(
                content=content,
                animal=self.object,
                user=request.user
            )

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



class AnimalAbandonedDetailView(generic.DetailView):   
    model = Animal
    context_object_name = 'animais'
    template_name = 'detail_abandoned.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_animal.filter(animal=self.object).order_by('dt_create')
        
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        content = request.POST.get('comment')
        comment_edit = request.POST.get('comment_edit')
        comment_id = request.POST.get('comment_id')

     
        if comment_id:
            print(comment_id, comment_edit)
            comentario = get_object_or_404(Comment, id=comment_id)
            comentario.content = comment_edit
            comentario.save()
        else:    
            Comment.objects.create(
                content=content,
                animal=self.object,
                user=request.user
            )

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

def excluir_comentario(request):
    if request.method == "POST":
        comment_id = request.POST.get("comment_id")
        comentario = get_object_or_404(Comment, id=comment_id)
        animal_id = comentario.animal.id
        comentario.delete()
    return redirect("animal_detail", pk=animal_id)


def teste_base(request):
    return render(request, 'base_h.html')

class AnimalUpdateView(generic.UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animals_update.html'
    context_object_name = 'media'
    success_url = reverse_lazy('user_profile')


class PictureUpdateView(generic.UpdateView):
    model = PictureGalery
    form_class = GaleryForm
    template_name = 'pictures_update.html'
    context_object_name = 'media'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pictures'] = PictureGalery.objects.filter(animal=self.object.id)
        
        return context
    

def pictureUpdate(request, pk):
    pictures = PictureGalery.objects.filter(animal=pk)
    print(pictures)

    if request.method == 'GET':
        print('metodo get')
        return render(request, 'pictures_update.html' ,{'pictures': pictures})
    elif request.method == 'POST':
        files = request.FILES.getlist('picture')
        print('POST')
        print(files)
        if files:
            for f in files:
                PictureGalery.objects.create(
                    picture=f,
                    animal= Animal.objects.get(id = pk)             
                )
        return render(request, 'pictures_update.html' ,{'pictures': pictures})
    
    return render(request, 'pictures_update.html' ,{'pictures': pictures})

def deletePicture(request, pk):
    if request.method == "GET":
        picture = get_object_or_404(PictureGalery, id=pk)
        id_animal = picture.animal_id
        picture.delete()
        # comentario = get_object_or_404(Comment, id=comment_id)
        # animal_id = comentario.animal.id
        # comentario.delete()

    # return redirect("animal_detail", pk=animal_id)
    return redirect("update_picture", pk=id_animal)
