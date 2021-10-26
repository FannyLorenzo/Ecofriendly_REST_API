
import pyrebase

config = {

  "apiKey": "AIzaSyBJNWrkN9j5FmXQt7sAdHk1CpORENSYo6Q",

  "authDomain": "ecofriendly-db.firebaseapp.com",

  "databaseURL": "https://ecofriendly-db-default-rtdb.firebaseio.com",

  "projectId": "ecofriendly-db",

  "storageBucket": "ecofriendly-db.appspot.com",

  "messagingSenderId": "110507311572",

  "appId": "1:110507311572:web:5de1b6ff6798397afe1641"

  # "measurementId": "G-434RL5YFF7"

}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

