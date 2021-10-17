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
        id = database.child('Cars').child('1').child('name').get().val()
        cars = database.child('Cars').get().val()
        
        arr_cars = []
        for item in cars:
            if item != None:
                arr_cars.append(Car(name=item.get('name'), top_speed=item.get('top_speed')))

        return arr_cars