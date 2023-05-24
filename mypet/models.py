from django.db import models

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.EmailField()




