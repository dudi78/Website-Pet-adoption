

from django.contrib.auth.models import AbstractUser
from django.db import models



class MyUser(AbstractUser):
    phone = models.CharField(max_length=20)



class Annonce(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown'),
    ]

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    nom_animal = models.CharField(max_length=255)
    espece = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    image1 = models.ImageField(upload_to='static/images/')
    image2 = models.ImageField(upload_to='static/images/')
    image3 = models.ImageField(upload_to='static/images/')
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
   
    def __str__(self):
        return self.nom_animal
    
