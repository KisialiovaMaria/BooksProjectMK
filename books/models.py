from django.db import models


# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name


# class Style(models.Model):
#     style_name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.style_name


class Book(models.Model):
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
