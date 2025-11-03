from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen, name='home'),
    path('cadastro-pet/',views.animal_cad_screen, name='animal_cad'),
    path('lista-pets/',views.animal_list_screen, name='animal_list'),
    path('lista-pets/<str:gender>',views.animal_list_screen_filt, name='animal_list'),
]