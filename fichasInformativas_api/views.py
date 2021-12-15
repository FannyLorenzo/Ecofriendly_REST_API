#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #para devolver respuestas http 400 por ejemplo

from fichasInformativas_api.models import FichaInformativa
import global_methods

class FichaInformativaApiView(APIView):

    def get(self, request):
        try:
            fichasInformativas = FichaInformativa.getFichaInformativa()
            return Response(fichasInformativas)
            
        except:
            return Response({"message": "Ocurrió un error"})


class FichaInformativaCreateApiView(APIView):

    def post(self, request):  
        try:
            validation = global_methods.validateToken(request.headers['Authorization'][7:])
            if validation['status'] == True and (validation['rol'] == "superadmin" or validation['rol'] == "admin"):  
                res = FichaInformativa.createFichaInformativa(request.data)
                return Response(res)
            return Response({"message": "Acceso no autorizado"})
        except:
            return Response({"message": "Ocurrió un error"})

class FichaInformativaDeleteApiView(APIView):
    
    def post(self, request):
        try:
            validation = global_methods.validateToken(request.headers['Authorization'][7:])
            if validation['status'] == True and (validation['rol'] == "superadmin" or validation['rol'] == "admin"):  
                res = FichaInformativa.deleteFichaInformativa(request.data)
                return Response(res)
            return Response({"message": "Acceso no autorizado"})
        except:
            return Response({"message": "Ocurrió un error"})

class FichaInformativaUpdateApiView(APIView):

    def post(self, request):
        try:
            validation = global_methods.validateToken(request.headers['Authorization'][7:])
            if validation['status'] == True and (validation['rol'] == "superadmin" or validation['rol'] == "admin"):  
                res = FichaInformativa.updateFichaInformativa(request.data)
                return Response(res)
            return Response({"message": "Acceso no autorizado"})
        except:
            return Response({"message": "Ocurrió un error"})

class FichaInformativaRetrieveApiView(APIView):

    def post(self, request):   
        try:
            validation = global_methods.validateToken(request.headers['Authorization'][7:])
            if validation['status'] == True and (validation['rol'] == "superadmin" or validation['rol'] == "admin"):  
                res = FichaInformativa.retrieveFichaInformativa(request.data)
                return Response(res)
            return Response({"message": "Acceso no autorizado"})
        except:
            return Response({"message": "Ocurrió un error"})