import pyrebase
from pprint import pprint
from .models import *

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


class FirebaseDB:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(config)
        self.authe = self.firebase.auth()
        self.database = self.firebase.database()

    def load_authors(self):
        Author.objects.all().delete()
        books_list = self.database.child('Data1').get().val()
        authors = set()
        for book in books_list.values():
            authors.add(book['author'])
        i = 0
        for author in authors:
            i += 1
            new_author = Author(id=i, name=author)
            new_author.save()
        print(Author.objects.all())

    def load_styles(self):
        Style.objects.all().delete()
        books_list = self.database.child('Data1').get().val()
        styles = set()
        for book in books_list.values():
            styles.add(book['style'])
        i = 0
        for style in styles:
            i += 1
            new_style = Style(id=i, name=style)
            new_style.save()
        print(Style.objects.all())

    def load_all_books(self):
        books_list = self.database.child('Data1').get().val()
        Book.objects.all().delete()
        i = 0
        for book in books_list.values():
            i += 1
            id = i
            author = book['author']
            description = book['description']
            mark = float(book['mark'])
            style = book['style']
            title = book['title']
            new_book = Book(id=id, author=author, description=description, mark=mark, style=style, title=title)
            new_book.save()
