from django.urls import path
from fichasInformativas_api import views

urlpatterns = [   
    path('fichas/', views.FichaInformativaApiView.as_view()),
    path('fichas/create/', views.FichaInformativaCreateApiView.as_view()),
    path('fichas/delete/', views.FichaInformativaDeleteApiView.as_view()),
    path('fichas/update/', views.FichaInformativaUpdateApiView.as_view()),
    path('fichas/retrieve/', views.FichaInformativaRetrieveApiView.as_view())

]