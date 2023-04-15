from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    Comments = models.IntegerField()
    Genres = models.IntegerField()
    Platforms = models.IntegerField()
    
    def __str__(self):
        return self.title