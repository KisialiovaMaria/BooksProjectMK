from django.db import models


class Book(models.Model):
    # id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    mark = models.FloatField(null=True)
    author = models.CharField(max_length=100)
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
