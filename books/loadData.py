import pyrebase
from pprint import pprint
from .models import *
config={
    "apiKey": "AIzaSyDbkT3XoBL-9-TSMj4qWRKUh8smd_Q2YYA",
    "authDomain": "booksearchproject-ff774.firebaseapp.com",
    "databaseURL": "https://booksearchproject-ff774-default-rtdb.firebaseio.com",
    "projectId": "booksearchproject-ff774",
    "storageBucket": "booksearchproject-ff774.appspot.com",
    "messagingSenderId": "89065194797",
    "appId": "1:89065194797:web:ac1dc9b3c1b9b8e7913fa4",
    "measurementId": "G-KRS2697HSW"
}

class FirebaseDB: 
    def __init__(self):
        self.firebase=pyrebase.initialize_app(config)
        self.authe = self.firebase.auth()
        self.database=self.firebase.database()

    def load_all_books(self):
        booksList = self.database.child('Data').get().val()
        Book.objects.all().delete()
        for book in booksList[1:]:
            id = book['id']
            author = book['author']
            description = book['description']
            mark = float(book['mark'])
            style = book['style']
            title = book['title']
            new_book = Book(id=id, author=author, description=description, mark = mark, style=style, title=title)
            new_book.save()
        

