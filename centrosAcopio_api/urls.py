from django.urls import path
from centrosAcopio_api import views

urlpatterns = [   
    path('centros/', views.CentroAcopioApiView.as_view()),
    path('centros/create/', views.CentroAcopioCreateApiView.as_view()),
    path('centros/delete/', views.CentroAcopioDeleteApiView.as_view()),
    path('centros/update/', views.CentroAcopioUpdateApiView.as_view()),
    path('centros/retrieve/', views.CentroAcopioRetrieveApiView.as_view())

]