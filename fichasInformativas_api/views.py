#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #para devolver respuestas http 400 por ejemplo

from fichasInformativas_api.models import FichaInformativa

class FichaInformativaApiView(APIView):

    def get(self, request):
        fichasInformativas = FichaInformativa.getFichaInformativa()
        return Response(fichasInformativas)


class FichaInformativaCreateApiView(APIView):

    def post(self, request):    
        res = FichaInformativa.createFichaInformativa(request.data)
        return Response(res)


class FichaInformativaDeleteApiView(APIView):
    
    def post(self, request):
        res = FichaInformativa.deleteFichaInformativa(request.data)
        return Response(res)

class FichaInformativaUpdateApiView(APIView):

    def post(self, request):    
        res = FichaInformativa.updateFichaInformativa(request.data)
        return Response(res)