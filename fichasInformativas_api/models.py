import global_methods
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
from db.db_connection import database

class FichaInformativa(models.Model):

    def getFichaInformativa():
        
        try:
            fichas = database.child('FichasInformativas').get()
            
            dict_fichas = {"data":[]}
            for item in fichas.each():
                if item != None:
                    dict_fichas["data"].append( 
                        { 
                            "id":item.val().get('id'),
                            "fecha":item.val().get('fecha'),
                            "titulo":item.val().get('titulo'),
                            "descripcion":item.val().get('descripcion'),
                            "url_imagen":item.val().get('url_imagen'),
                            "tipo":item.val().get('tipo'),
                            "detalle":item.val().get('detalle'),
                        })
            return dict_fichas  

        except:
            return {"message":"Ocurrió un error"}

    def createFichaInformativa(data):
        try:
            data = {
                "id":global_methods.uuid_generator(),
                "fecha":data["fecha"],
                "titulo":data["titulo"],
                "descripcion":data["descripcion"],
                "url_imagen":data["url_imagen"],
                "tipo":data["tipo"],
                "detalle":data["detalle"],
            }
        
            if database.child('FichasInformativas').child(data["id"]).get().val():
                return {"message": "Esta ficha ya existe"}
            else:
                database.child('FichasInformativas').child(data["id"]).set(data)
                return {"message": "Agregada exitosamente"}
        except:
            return {"message":"Ocurrió un error"}

    
    def deleteFichaInformativa(data):
        try:
        
            if database.child('FichasInformativas').child(data["id"]).get().val():
                database.child('FichasInformativas').child(data["id"]).remove()
                return {"message": "Ficha eliminada exitosamente"}
            else:
                return {"message": "Esta ficha no existe!"}
        except:
            return {"message":"Ocurrió un error"}
    
    def updateFichaInformativa(data):
        try:
            data = {
                "id":data["id"],
                "fecha":data["fecha"],
                "titulo":data["titulo"],
                "descripcion":data["descripcion"],
                "url_imagen":data["url_imagen"],
                "tipo":data["tipo"],
                "detalle":data["detalle"],  # array de strings
            }
        
            if database.child('FichasInformativas').child(data["id"]).get().val():
                database.child('FichasInformativas').child(data["id"]).set(data)
                return {"message": "Datos de ficha modificados", "actual": data}
            else:
                return {"message": "Esta ficha no existe"}
        except:
            return {"message":"Ocurrió un error"}  


    
