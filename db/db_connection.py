
import pyrebase

config = {
  "apiKey": "AIzaSyC5faofrC7kfBpp7RSX9O3iOkRucNmCNSc",

  "authDomain": "recicla-aqp-app.firebaseapp.com",

  "databaseURL": "https://recicla-aqp-app-default-rtdb.firebaseio.com",

  "projectId": "recicla-aqp-app",

  "storageBucket": "recicla-aqp-app.appspot.com",

  "messagingSenderId": "1093377891879",

  "appId": "1:1093377891879:web:e1b79358463d9e25a57802",

#   "measurementId": "G-VZRC6QG6GX"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

