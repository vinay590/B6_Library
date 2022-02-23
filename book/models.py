from django.db import models

# Create your models here.
print("in models.py")
class ActiveBooks(models.Manager):
    def get_queryset(self):
        return super(ActiveBooks, self).get_queryset().filter(is_active="Y")         ####Custom manager

class InActiveBooks(models.Manager):
    def get_queryset(self):
        return super(InActiveBooks, self).get_queryset().filter(is_active="N")      ########## Cutom Manager

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_active = models.CharField(max_length=1, default="Y")
    active_books = ActiveBooks()     ###  active books 
    inactive_books = InActiveBooks()  ### Inactive Books
    objects = models.Manager()      #### Default manager
 
    class Meta:
        db_table = "book"

    def __str__(self):
        return f"{self.name}"

#######Pagination (Blog Example)
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    publish_date = models.DateTimeField()

    def __str__(self):
        return f"Title {self.title}-----{self.publish_date}"


class Employee(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    class Meta:
        db_table = "emp"

    def __str__(self):
        return f"{self.name}"
