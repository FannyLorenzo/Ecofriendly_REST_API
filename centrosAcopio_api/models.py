from django.db import models

# Create your models here.
from db.db_connection import database

# MODELO (CARRO DE PRUEBA)
class Car(models.Model):
    name = models.CharField(max_length=200)
    top_speed = models.IntegerField()

    # OBTENER TODOS LOS REGISTROS DE LA TABLA CARS
    def getCars():

        #
        # FORMA 2 Y DEVUELVE UN DICCIONARIO (NO UTILIZA OBJETOS)
        #
        cars = database.child('Cars').get().val()
        
        dict_cars = {"data":[]}
        for item in cars:
            if item != None:
                # arr_cars.append(Car(name=item.get('name'), top_speed=item.get('top_speed')))
                dict_cars["data"].append( { "car_name":item.get('name'), "car_top_spe":item.get('top_speed')})
        return dict_cars

