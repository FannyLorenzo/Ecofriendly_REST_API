from uuid import uuid4
from db.db_connection import database

def uuid_generator():
    return uuid4().hex

def validateToken(token):
    try:
        usuarios = database.child('Usuarios').get()

        for item in usuarios.each():
            if item != None:
                if token == item.val().get('token'):
                    return {"status":True, "rol":item.val().get('rol')}

        return {"status":False, "rol":"nadie"}  

    except:
        return {"status":False, "rol":"nadie"}
