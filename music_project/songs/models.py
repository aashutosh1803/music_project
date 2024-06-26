from django.db import models

class Song(models.Model):
    index = models.AutoField(primary_key=True)
    id = models.CharField(max_length=31,editable=False)
    title = models.CharField(max_length=64)
    danceability = models.FloatField(null=True)
    energy = models.FloatField(null=True)
    key = models.IntegerField(null=True)
    loudness = models.FloatField(null=True)
    mode = models.IntegerField(null=True)
    acousticness = models.FloatField(null=True)
    instrumentalness = models.FloatField(null=True)
    liveness = models.FloatField(null=True)
    valence = models.FloatField(null=True)
    tempo = models.FloatField(null=True)
    duration_ms = models.IntegerField(null=True)
    time_signature = models.IntegerField(null=True)
    num_bars = models.IntegerField(null=True)
    num_sections = models.IntegerField(null=True)
    num_segments = models.IntegerField(null=True)
    song_class = models.IntegerField(null=True)
    rating = models.FloatField(null=True, blank=True)
