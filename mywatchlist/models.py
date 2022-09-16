from django.db import models

class MyWatchlist(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.FloatField(max_length=5)
    release_date = models.DateField()
    review = models.TextField()