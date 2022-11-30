import json

import pyrebase

config = {
    "apiKey": "AIzaSyDbkT3XoBL-9-TSMj4qWRKUh8smd_Q2YYA",
    "authDomain": "booksearchproject-ff774.firebaseapp.com",
    "databaseURL": "https://booksearchproject-ff774-default-rtdb.firebaseio.com",
    "projectId": "booksearchproject-ff774",
    "storageBucket": "booksearchproject-ff774.appspot.com",
    "messagingSenderId": "89065194797",
    "appId": "1:89065194797:web:ac1dc9b3c1b9b8e7913fa4",
    "measurementId": "G-KRS2697HSW"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
with open("D:/univer/7sem/OITIPU/projectMK/books/info.json", encoding="utf-8") as f:
    info = json.load(f)
# info = database.child('Data').get()
# for i in info.each():
#     print(i.val())
for book in info['info']:
    database.child('Data1').push(book)


