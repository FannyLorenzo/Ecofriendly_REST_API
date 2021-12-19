from django.urls import path
from huellaEcologica_api import views

urlpatterns = [   
    path('huella/', views.HuellaEcologicaApiView.as_view()),
    path('huella/anio/', views.HuellaEcologicaXanioApiView.as_view()),
    path('huella/ambito/', views.HuellaEcologicaXambitoApiView.as_view()),
    path('huella/prediccion/', views.HuellaEcologicaPrediccionApiView.as_view()),

]