#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #para devolver respuestas http 400 por ejemplo

from profiles_api import serializers

from profiles_api.models import Car

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


from django.core import serializers

class CarApiView(APIView):  
    
    def get(self, request):
        
        #MANERA 1
        # cars = Car.getCars()
        # # data = serializers.serialize('json', [cars, ])
        # # struct = json.loads(data)
        # # data = json.dumps(struct[0])
        # return Response(serializers.serialize('json', cars))
    
        #MANERA 2

        cars = Car.getCars()
        return Response(cars)

from profiles_api.models import Usuario

class UsuarioApiView(APIView):

    def get(self, request):
        usuarios = Usuario.getUsuarios()
        return Response(usuarios)


class UsuarioCreateApiView(APIView):

    def post(self, request):    
        res = Usuario.createUsuario(request.data)
        return Response(res)


class UsuarioDeleteApiView(APIView):
    
    def post(self, request):
        res = Usuario.deleteUsuario(request.data)
        return Response(res)

class UsuarioUpdateApiView(APIView):

    def post(self, request):    
        res = Usuario.updateUsuario(request.data)
        return Response(res)