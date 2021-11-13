#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #para devolver respuestas http 400 por ejemplo

from centrosAcopio_api.models import CentroAcopio


class CentroAcopioApiView(APIView):
    def get(self, request):
        centroAcopios = CentroAcopio.getCentrosAcopio()
        return Response(centroAcopios)


class CentroAcopioCreateApiView(APIView):

    def post(self, request):    
        res = CentroAcopio.createCentroAcopio(request.data)
        return Response(res)


class CentroAcopioDeleteApiView(APIView):
    
    def post(self, request):
        res = CentroAcopio.deleteCentroAcopio(request.data)
        return Response(res)

class CentroAcopioUpdateApiView(APIView):

    def post(self, request):    
        res = CentroAcopio.updateCentroAcopio(request.data)
        return Response(res)

class CentroAcopioRetrieveApiView(APIView):

    def post(self, request):    
        res = CentroAcopio.retrieveCentroAcopio(request.data)
        return Response(res)