""" Funciona bajo un ambiente virtual de trabajo con las Versiones utilizadas """
python 3.9.7
django 3.2.7
djangorestframework 3.12.4

""" INICIO """
Activar el ambiente de trabajo instalado y correr el proyecto
ambiente> Scripts/activate.bat
(ambiente) E:\APLICACIONES\PROYECTO_TAIS\Proyecto_Back\ambiente> cd REST_API
(ambiente) E:\APLICACIONES\PROYECTO_TAIS\Proyecto_Back\ambiente\REST_API> python manage.py runserver

""" Se puede acceder a modo de prueba a los siguientes urls: """
http://127.0.0.1:8000/api/admin/
http://127.0.0.1:8000/api/hello/ (aqui el minicrud de prueba)
http://127.0.0.1:8000/api/admin/profiles_api/userprofile/


""" Crear superusuario: """
REST_API> python manage.py createsuperuser

""" IMPORTANTE """
Cada que se modifique models.py en cada modulo, hacer: 
REST_API> python manage.py makemigrations [nombre del modulo]
REST_API> python manage.py migrate

ejemplo: python manage.py makemigrations profiles_api
y luego  python manage.py migrate


posdata:
CURSO SEGUIDO: https://www.youtube.com/watch?v=Z8ADAr9KZYc 

