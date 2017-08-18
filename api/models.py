from django.db import models

from blood_alert.models import Alert

# Create your models here.

class Centres(models.Model):
    lieu = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    qteDisponible = models.IntegerField()

class Articles(models.Model):
    title = models.CharField(max_length=255)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date posted')
    photo = models.ImageField(blank=True)

class Statistique(models.Model):
    critere = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date posted')
    pourcentage = models.IntegerField()

    def get_pourcentage(self):
        return self.pourcentage + "%"
