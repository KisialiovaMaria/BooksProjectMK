import graphene
from graphene_django import DjangoObjectType
from .models import *
from .loadData import *



#here we are doing firebase authentication


class BookType(DjangoObjectType):
    class Meta:
        model = Book

# fdb = FirebaseDB()

class Query(graphene.ObjectType):
    
    allBooks = graphene.List(BookType)

    # books = graphene.List(BookType)
    booksByParams = graphene.List(BookType, author=graphene.String(), style=graphene.String(), title=graphene.String())
    # booksUpdate = graphene.List(BookType, )

    # def resolve_author(self, info, **kwargs):

    #     id = kwargs.get('id')
    #     if id is not None:
    #         return Author.objects.get(pk=id)
    #     return None

    # def resolve_book(self, info, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return Book.objects.get(pk=id)
    #     return None

    # def resolve_books(self, info, **kwargs):
    #     return Book.objects.all()

    def resolve_allBooks(self, info, **kwargs):
        return Book.objects.all()


    def resolve_booksByParams(self, info, **kwargs):
        author=kwargs.get('author')
        style=kwargs.get('style')
        title=kwargs.get('title')
        if author is None or style is None:
            return None
        else:
            return Book.objects.filter(author=author, style=style, title__icontains=title)

fdb = FirebaseDB()
fdb.load_all_books()
schema = graphene.Schema(query=Query)

