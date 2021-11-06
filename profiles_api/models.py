from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manager para perfiles de usuario """
    def create_user(self, email, name, password=None):
        """ crear Nuevo user profile """
        if not email:
            raise ValueError('Usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo base de datos para usuarios en el sistema """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ obtener nombre completo"""
        return self.name
    
    def get_short_name(self):
        """ obtener nombre completo"""
        return self.email

# Create your models here.
from db.db_connection import database

# MODELO (CARRO DE PRUEBA)
class Car(models.Model):
    name = models.CharField(max_length=200)
    top_speed = models.IntegerField()

    # OBTENER TODOS LOS REGISTROS DE LA TABLA CARS
    def getCars():

        #
        # FORMA 1 Y DEVUELVE UN STRING LARGO QUE DEBERIA SER JSON
        #

        # id = database.child('Cars').child('1').child('name').get().val()
        # cars = database.child('Cars').get().val()
        
        # arr_cars = []
        # for item in cars:
        #     if item != None:
        #         arr_cars.append(Car(name=item.get('name'), top_speed=item.get('top_speed')))

        # return arr_cars

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

class Usuario(models.Model):

    def getUsuarios():
        
        try:
            usuarios = database.child('Usuarios').get().val()
            
            dict_usuarios = {"data":[]}
            for item in usuarios:
                if item != None:
                    # arr_cars.append(Car(name=item.get('name'), top_speed=item.get('top_speed')))
                    dict_usuarios["data"].append( 
                        { 
                            "apellido":item.get('apellido'), 
                            "email":item.get('email'),
                            "estado":item.get('estado'),
                            "id":item.get('id'),
                            "nombre":item.get('nombre'),
                            "rol":item.get('rol'),
                        })
            return dict_usuarios  

        except:
            return {"message":"Ocurrió un error"}

    def createUsuario(data):
        try:
            data = {
                "id": data["id"],
                "apellido": data["apellido"],
                "email": data["email"],
                "estado": data["estado"],
                "nombre": data["nombre"],
                "password": data["password"],
                "rol": data["rol"]
            }
        
            if database.child('Usuarios').child(data["id"]).get().val():
                return {"message": "Este usuario ya esta creado"}
            else:
                database.child('Usuarios').child(data["id"]).set(data)
                return {"message": "Agregado exitosamente"}
        except:
            return {"message":"Ocurrió un error"}
        # data = {
        #     "id" : "3",
        #     "name" : "carro morado",
        #     "top_speed" : "43"
        # }
        # database.child('Cars').child('3').set(data)
    
    def deleteUsuario(data):
        try:
        
            if database.child('Usuarios').child(data["id"]).get().val():
                database.child('Usuarios').child(data["id"]).remove()
                return {"message": "Usuario eliminado exitosamente"}
            else:
                return {"message": "Este usuario no existe!"}
        except:
            return {"message":"Ocurrió un error"}
    
    def updateUsuario(data):
        try:
            data = {
                "id": data["id"],
                "apellido": data["apellido"],
                "email": data["email"],
                "estado": data["estado"],
                "nombre": data["nombre"],
                "password": data["password"],
                "rol": data["rol"]
            }
        
            if database.child('Usuarios').child(data["id"]).get().val():
                database.child('Usuarios').child(data["id"]).set(data)
                return {"message": "Datos modificados"}
            else:
                return {"message": "Este registro no existe"}
        except:
            return {"message":"Ocurrió un error"}
