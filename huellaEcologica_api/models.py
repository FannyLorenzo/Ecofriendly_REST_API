
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
from db.db_connection import database
#from django.db.models import historicoHuella

import json

class HuellaEcologica(models.Model):  


    def getHistoricoHuella_anio(entrada):
            # Load the data into a list.
        data = {}
        filename = 'dataJSONok.json'
        anio = entrada['anio']

        data["anio"] = anio
        data['contenido'] = []

        with open(filename) as f:
            pop_data = json.load(f)

        for pop_dict in pop_data:
            if pop_dict['anio'] == anio:
                nombre_departamento = pop_dict['ambito']                
                area_de_cultivos = pop_dict['area_de_cultivos']
                area_de_pastoreo = pop_dict['area_de_pastoreo']
                area_de_bosques = pop_dict['area_de_bosques']
                zonas_de_pesca = pop_dict["zonas_de_pesca "]
                huella_de_carbono = pop_dict['huella_de_carbono']
                areas_urbanas = pop_dict['areas_urbanas']
                huella_regional_percapita = pop_dict['huella_regional_percapita']
                salida = {                          
                            "ambito": nombre_departamento,
                            "area_de_cultivos": area_de_cultivos,
                            "area_de_pastoreo": area_de_pastoreo,
                            "area_de_bosques": area_de_bosques,
                           "zonas_de_pesca ": zonas_de_pesca,
                            "huella_de_carbono": huella_de_carbono,
                            "areas_urbanas": areas_urbanas,
                            "huella_regional_percapita": huella_regional_percapita                        
                         }
                         
                data['contenido'].append(salida)

                #print(f"{nombre_departamento}: {huella_percapita}")

        return data
    
    def getHistoricoHuella_ambito(entrada):
            # Load the data into a list.
        data = {}
        filename = 'dataJSONok.json'
        cod_ambito = entrada['cod_ambito']

        data['cod_ambito'] = cod_ambito
        data['ambito'] = ''
        data['contenido'] = []

        with open(filename) as f:
            pop_data = json.load(f)

        for pop_dict in pop_data:
            if pop_dict['cod_ambito'] == cod_ambito:
                
                anio = pop_dict['anio']                
                data['ambito'] = pop_dict['ambito'] 
                area_de_cultivos = pop_dict['area_de_cultivos']
                area_de_pastoreo = pop_dict['area_de_pastoreo']
                area_de_bosques = pop_dict['area_de_bosques']
                zonas_de_pesca = pop_dict["zonas_de_pesca "]
                huella_de_carbono = pop_dict['huella_de_carbono']
                areas_urbanas = pop_dict['areas_urbanas']
                huella_regional_percapita = pop_dict['huella_regional_percapita']
                salida = {                          
                            "anio": anio,
                            "area_de_cultivos": area_de_cultivos,
                            "area_de_pastoreo": area_de_pastoreo,
                            "area_de_bosques": area_de_bosques,
                            "zonas_de_pesca ": zonas_de_pesca,
                            "huella_de_carbono": huella_de_carbono,
                            "areas_urbanas": areas_urbanas,
                            "huella_regional_percapita": huella_regional_percapita                        
                         }
                         
                data['contenido'].append(salida)

                #print(f"{nombre_departamento}: {huella_percapita}")

        return data

    def getHistoricoHuella():
    # JSON file
        try:
            f = open ("dataJSONok.json", "r")
            
            # Reading from file
            data = json.loads(f.read())
            return {"message":"exito",
            "contenido": data
            }
        except Exception as e :
            return {"message":e
            }

    def prediccionHuella(data):
        anio = data["anio"]
        cod_ambito = data["cod_ambito"]
        ambito = ''
        a = 0
        b = 0
        presicion = 0
        huella_regional_percapita = 0

        try:
            with open("modelo.json") as f:
             pop_data = json.load(f)

            for pop_dict in pop_data:
                if pop_dict['cod_ambito'] == cod_ambito:
                   ambito = pop_dict['ambito']
                   a = pop_dict['a']
                   b = pop_dict['b']
                   presicion = pop_dict['presicion']
                   huella_regional_percapita = a*(anio-2010) + b                   
                
            salida = {
                        "anio":anio,
                        "cod_ambito": cod_ambito,
                        "ambito": ambito,
                        "coef_a": a,
                        "coef_b": b,
                        "presicion": presicion,
                        "huella_predicta" : huella_regional_percapita
                    }
                   
            
            
            return {
                "message":"Predicción realizada",
                "resultado": salida                
            }
        
        except Exception as e :
            return {"message":e
            }
        

