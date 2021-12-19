#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #para devolver respuestas http 400 por ejemplo

from huellaEcologica_api.models import HuellaEcologica
import global_methods

class HuellaEcologicaApiView(APIView):

    def get(self, request):
        try:
            historicoHuellas = HuellaEcologica.getHistoricoHuella()
            return Response(historicoHuellas)
            
        except:
            return Response({"message": "Ocurrió un error"})

class HuellaEcologicaXanioApiView(APIView):

    def post(self, request):
        try:
            res = HuellaEcologica.getHistoricoHuella_anio(request.data)
            return Response(res)
            
        except:
            return Response({"message": "Ocurrió un error"})

class HuellaEcologicaXambitoApiView(APIView):

    def post(self, request):
        try:
            res = HuellaEcologica.getHistoricoHuella_ambito(request.data)
            return Response(res)
            
        except:
            return Response({"message": "Ocurrió un error"})

class HuellaEcologicaPrediccionApiView(APIView):

    def post(self, request):
        try:
            res = HuellaEcologica.prediccionHuella(request.data)
            return Response(res)
            
        except:
            return Response({"message": "Ocurrió un error"})