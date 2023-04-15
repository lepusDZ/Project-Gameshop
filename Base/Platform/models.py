from django.db import models

class Platforms(models.Model):
    name = models.CharField(max_length=150)
    Games = models.IntegerField()
    
    def __str__(self):
        return self.title