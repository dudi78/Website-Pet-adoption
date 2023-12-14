from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    phone = models.CharField(max_length=20)

import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('static/images2/', filename)


class annonce(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
       
    ]
     
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    nom_animal = models.CharField(max_length=255)
    espece = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
