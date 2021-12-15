#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #para devolver respuestas http 400 por ejemplo

from centrosAcopio_api.models import CentroAcopio
import global_methods

class CentroAcopioApiView(APIView):
    def get(self, request):
        try:
            centroAcopios = CentroAcopio.getCentrosAcopio()
            return Response(centroAcopios)
            
        except:
            return Response({"message": "Ocurrió un error"})


class CentroAcopioCreateApiView(APIView):

    def post(self, request):    
        try:
            validation = global_methods.validateToken(request.headers['Authorization'][7:])
            if validation['status'] == True and (validation['rol'] == "superadmin" or validation['rol'] == "admin"):  
                res = CentroAcopio.createCentroAcopio(request.data)
                return Response(res)
            return Response({"message": "Acceso no autorizado"})
        except:
            return Response({"message": "Ocurrió un error"})

class CentroAcopioDeleteApiView(APIView):
    
    def post(self, request):
        try:
            validation = global_methods.validateToken(request.headers['Authorization'][7:])
            if validation['status'] == True and (validation['rol'] == "superadmin" or validation['rol'] == "admin"): 
                res = CentroAcopio.deleteCentroAcopio(request.data)
                return Response(res)
            return Response({"message": "Acceso no autorizado"})
        except:
            return Response({"message": "Ocurrió un error"})

class CentroAcopioUpdateApiView(APIView):

    def post(self, request):   
        try:
            validation = global_methods.validateToken(request.headers['Authorization'][7:])
            if validation['status'] == True and (validation['rol'] == "superadmin" or validation['rol'] == "admin"):   
                res = CentroAcopio.updateCentroAcopio(request.data)
                return Response(res)
            return Response({"message": "Acceso no autorizado"})
        except:
            return Response({"message": "Ocurrió un error"})

class CentroAcopioRetrieveApiView(APIView):

    def post(self, request):  
        try:
            validation = global_methods.validateToken(request.headers['Authorization'][7:])
            if validation['status'] == True and (validation['rol'] == "superadmin" or validation['rol'] == "admin"):   
                res = CentroAcopio.retrieveCentroAcopio(request.data)
                return Response(res)
            return Response({"message": "Acceso no autorizado"})
        except:
            return Response({"message": "Ocurrió un error"})