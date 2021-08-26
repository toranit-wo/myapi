from django.db import models

class Apis(models.Model):
    title = models.CharField(max_length=100,default='')
    data = models.TextField(default='')

class Forehand (models.Model):
    counter = models.IntegerField(default=0)
    tmor = models.FloatField(default=0)
    cra = models.FloatField(default=0)
    tmcr = models.FloatField(default=0)

class Backhand (models.Model):
    counter = models.IntegerField(default=0)
    tmor = models.FloatField(default=0)
    cra = models.FloatField(default=0)
    tmcr = models.FloatField(default=0)