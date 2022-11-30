import graphene
from graphene_django import DjangoObjectType
from .models import *
from .loadData import *


# here we are doing firebase authentication


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class StyleType(DjangoObjectType):
    class Meta:
        model = Style


class Query(graphene.ObjectType):
    allStyles = graphene.List(StyleType)
    allBooks = graphene.List(BookType)
    allAuthors = graphene.List(AuthorType)
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
    def resolve_allAuthors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_allStyles(self, info, **kwargs):
        return Style.objects.all()

    def resolve_allBooks(self, info, **kwargs):
        return Book.objects.all()

    def resolve_booksByParams(self, info, **kwargs):
        author = kwargs.get('author')
        style = kwargs.get('style')
        title = kwargs.get('title')
        if author and style:
            return Book.objects.filter(author=author, style=style, title__icontains=title)
        elif author and not style:
            return Book.objects.filter(author=author, title__icontains=title)
        elif not author and style:
            return Book.objects.filter(style=style, title__icontains=title)
        if not author and not style:
            return Book.objects.filter(title__icontains=title)



fdb = FirebaseDB()
fdb.load_all_books()
fdb.load_authors()
fdb.load_styles()
schema = graphene.Schema(query=Query)
