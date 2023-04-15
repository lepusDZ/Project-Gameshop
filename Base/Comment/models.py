from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    gameID = models.IntegerField()
    replies = models.IntegerField()
    
    def __str__(self):
        return self.title