from django.db import models

# Create your models here.
from db.db_connection import database

# MODELO (CARRO DE PRUEBA)
class CentroAcopio(models.Model):

    # OBTENER TODOS LOS REGISTROS DE LA TABLA CARS
    def getCentrosAcopio():
        try:
            centros = database.child('CentroAcopio').get().val()
            
            dict_centros = {"data":[]}
            for item in centros:
                if item != None:
                    dict_centros["data"].append( 
                        { 
                            "id":item.get('id'),
                            "descripcion":item.get('descripcion'),
                            "direccion":item.get('direccion'),
                            "estado":item.get('estado'),
                            "horario":item.get('horario'),
                            "latitud":item.get('latitud'),
                            "longitud":item.get('longitud'),
                            "nombre":item.get('nombre'),
                            "telefono":item.get('telefono')
                        })
            return dict_centros

        except:
            return {"message":"Ocurrió un error"}
    

    def createCentroAcopio(data):
        try:
            data = {
                "id":data["id"],
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
                return {"message": "Ficha eliminada exitosamente"}
            else:
                return {"message": "Esta ficha no existe!"}
        except:
            return {"message":"Ocurrió un error"}

    def updateCentroAcopio(data):
        try:
            data = {
                "id":data["id"],
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
                return {"message": "Datos de ficha modificados", "actual": data}
            else:
                return {"message": "Esta ficha no existe"}
        except:
            return {"message":"Ocurrió un error"}  