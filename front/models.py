from django.db import models
from django.db.models import Avg, Count, Max, Min, Sum, F, Q


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    class Meta:
        db_table = 'front_author'


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'front_publisher'


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    pages = models.IntegerField()
    rating = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'front_book'


class BookOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        db_table = 'front_book_order'
