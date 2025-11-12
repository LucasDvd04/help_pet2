from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

##Crud usuario
class UserCreateView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'user_create.html'
    success_url = '/user-login/'


def UserLoginView(request):
    # form_class = AuthenticationForm
    # template_name = 'user_login.html'

    # def login(request):
        # ...
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)

        if user is not None:
            print('logado com sucesso')
            login(request, user)
            return redirect('home')
        else:
            print('vacilão')
            form = AuthenticationForm()

    return render(request, 'user_login.html',{'form':form})

    

class UserUpdateView(generic.UpdateView):

    ...
class UserDetailView(generic.DetailView):

    ...
class UserDeleteView(generic.DeleteView):
    ...

def logout_view(request):
    logout(request)
    return redirect('user_log')

