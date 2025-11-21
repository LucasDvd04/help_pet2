from django.urls import path
from accounts import views as acc
from . import views

urlpatterns = [
    path('', views.home_screen, name='home'),
    path('user-create/', acc.UserCreateView.as_view(), name='user_cad'),
    path('user-login/', acc.UserLoginView, name='user_log'),
    path('user-logout/', acc.logout_view, name='user_out'),
    path('cadastro-pet/',views.animal_cad_screen, name='animal_cad'),
    path('lista-lost/',views.animal_lost_screen, name='lost_list'),
    path('lista-adoct/',views.animal_adoction_screen, name='adoct_list'),
    path('lista-abandoned/',views.animal_abandoned_screen, name='abandoned_list'),
    path('del_comment/',views.excluir_comentario, name='comment_delete'),
    path('lista-lost/<int:pk>/detail',views.AnimalLostDetailView.as_view(), name='lost_detail'),
    path('lista-adoct/<int:pk>/detail',views.AnimalAdoctDetailView.as_view(), name='adoct_detail'),
    path('lista-abandoned/<int:pk>/detail',views.AnimalAbandonedDetailView.as_view(), name='abandoned_detail'),
    path('profile/update/',views.AnimalUpdateView.as_view(), name='update_animal'),
    path('profile/update/<int:pk>/',views.AnimalUpdateView.as_view(), name='update_animal'),
    path('profile/pictures/<int:pk>/',views.PictureUpdateView.as_view(), name='update_picture'),
    path('profile/pictures/<int:pk>/',views.PictureUpdateView.as_view(), name='update_picture'),
    path('teste-base/', views.teste_base, name='teste_base'),
]