import global_methods
from django.db import models 

# Create your models here.
from db.db_connection import database

class CentroAcopio(models.Model):


    def getCentrosAcopio():
        try:
            centros = database.child('CentroAcopio').get()
            
            dict_centros = {"data":[]}
            for item in centros.each():
                if item != None:    
                    dict_centros["data"].append( 
                        { 
                            "id":item.val().get('id'),
                            "categoria":item.val().get('categoria'),
                            "descripcion":item.val().get('descripcion'),
                            "direccion":item.val().get('direccion'),
                            "estado":item.val().get('estado'),
                            "horario":item.val().get('horario'),
                            "latitud":item.val().get('latitud'),
                            "longitud":item.val().get('longitud'),
                            "nombre":item.val().get('nombre'),
                            "telefono":item.val().get('telefono')
                            
                        })
                    
            return dict_centros

        except:
            return {"message":"Ocurrió un error"}
    

    def createCentroAcopio(data):
        try:
            data = {
                "id":global_methods.uuid_generator(),
                "categoria":data['categoria'],
                "descripcion":data['descripcion'],
                "direccion":data['direccion'],
                "estado":data['estado'],
                "horario":data['horario'],
                "latitud":data['latitud'],
                "longitud":data['longitud'],
                "nombre":data['nombre'],
                "telefono":data['telefono']
            }
        
            if database.child('CentroAcopio').child(data["id"]).get().val():
                return {"message": "Este centro ya existe"}
            else:
                database.child('CentroAcopio').child(data["id"]).set(data)
                return {"message": "Agregado exitosamente"}
        except:
            return {"message":"Ocurrió un error"}

    def deleteCentroAcopio(data):
        try:
        
            if database.child('CentroAcopio').child(data["id"]).get().val():
                database.child('CentroAcopio').child(data["id"]).remove()
                return {"message": "Centro eliminada exitosamente"}
            else:
                return {"message": "Este centro no existe!"}
        except:
            return {"message":"Ocurrió un error"}

    def updateCentroAcopio(data):
        try:
            data = {
                "id":data["id"],
                "categoria":data['categoria'],
                "descripcion":data['descripcion'],
                "direccion":data['direccion'],
                "estado":data['estado'],
                "horario":data['horario'],
                "latitud":data['latitud'],
                "longitud":data['longitud'],
                "nombre":data['nombre'],
                "telefono":data['telefono']
            }
        
            if database.child('CentroAcopio').child(data["id"]).get().val():
                database.child('CentroAcopio').child(data["id"]).set(data)
                return {"message": "Datos de centro modificados", "actual": data}
            else:
                return {"message": "Este centro no existe"}
        except:
            return {"message":"Ocurrió un error"}  