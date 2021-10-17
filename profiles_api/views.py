#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #para devolver respuestas http 400 por ejemplo

from profiles_api import serializers

""" API View de Prueba  """
class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """ Retornar la lista de caracteristicas del APIView """
        an_apiview = [
            'Usamos metodos HTTP como funciona (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de DJango',
            'Nos da el mayor control sobre ñla lógica de nuestra aplicación',
            'Esta mapeado manualmente a los URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=request.data) #contiene los datos que se requirieron

        if serializer.is_valid():
            name = serializer.validated_data.get('name') #campo 1
            message = f'Hello {name}'                    #campo 2
            return Response({'message':message}) # siempre en diccionario
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """ maneja actualizar un objeto"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """ maneja actualización parcial de un objeto """
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """ borrar un objeto"""
        return Response({'method': 'DELETE'})
    
    
    
