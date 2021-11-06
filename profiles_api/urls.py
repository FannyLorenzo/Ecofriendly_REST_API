from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello/', views.HelloApiView.as_view(), name='hello'), # ejemplo
    path('cars/', views.CarApiView.as_view()),
    path('usuarios/', views.UsuarioApiView.as_view()),
    path('usuarios/create/', views.UsuarioCreateApiView.as_view()),
    path('usuarios/delete/', views.UsuarioDeleteApiView.as_view()),
    path('usuarios/update/', views.UsuarioUpdateApiView.as_view())
# editar
# validar
]