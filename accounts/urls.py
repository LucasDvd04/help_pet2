from django.urls import path
from . import views 

urlpatterns = [
    path('user-create/', views.UserCreateView.as_view(), name='user_cad'),
    path('user-login/', views.UserLoginView, name='user_log'),
    path('user-logout/', views.logout_view, name='user_out'),
    path('profile/', views.profile_view, name='user_profile'),
   
]