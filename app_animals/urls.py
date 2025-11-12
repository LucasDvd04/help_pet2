from django.urls import path
from accounts import views as acc
from . import views

urlpatterns = [
    path('', views.home_screen, name='home'),
    path('user-create/', acc.UserCreateView.as_view(), name='user_cad'),
    path('user-login/', acc.UserLoginView, name='user_log'),
    path('user-logout/', acc.logout_view, name='user_out'),
    path('cadastro-pet/',views.animal_cad_screen, name='animal_cad'),
    # path('cadastro-pet/',views.AnimaCadView.as_view(), name='animal_cad'),
    # path('lista-pets/',views.AnimalsListView.as_view(), name='animal_list'),
    path('lista-pets/',views.animal_list_screen, name='animal_list'),
    path('del_comment/',views.excluir_comentario, name='comment_delete'),
    path('lista-pets/<int:pk>/detail',views.AnimalDetailView.as_view(), name='animal_detail'),
]