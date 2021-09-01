from django.db import models

class Forehand(models.Model):
    title = models.CharField(max_length=40)
    hits = models.IntegerField(default=0)
    over = models.FloatField(default=0)
    under = models.FloatField(default=0)
    good = models.FloatField(default=0)

    def __str__(self):
        return self.hits

class Backhand(models.Model):
    title = models.CharField(max_length=40)
    hits = models.IntegerField(default=0)
    over = models.FloatField(default=0)
    under = models.FloatField(default=0)
    good = models.FloatField(default=0)

    def __str__(self):
        return self.hits


