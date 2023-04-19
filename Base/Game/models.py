from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    comment = models.ForeignKey('Comment', on_delete = models.PROTECT, null = True)
    genre = models.ForeignKey('Genre', on_delete = models.PROTECT, null = True)
    platform = models.ForeignKey('Platform', on_delete = models.PROTECT, null = True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Games'
    

class Genre(models.Model):
    name = models.CharField(max_length=150)
    games = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Genres'
    
class Platform(models.Model):
    name = models.CharField(max_length=150)
    games = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Platforms'
    
class Comment(models.Model):
    name = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    gameID = models.IntegerField()
    replies = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Comments'