from django.db import models


# Create your models here.
class Accounts(models.Model):

    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)


# Create your models here.
class JsonData(models.Model):

    objects = None
    userid = models.IntegerField()
    title = models.CharField(max_length=254)
    body = models.TextField()

