from django.contrib import admin

from .models import Game, Genre, Platform, Comment


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'comment', 'genre', 'platform')
    search_fields = ('name', 'description')
    list_editable = ('genre', 'platform')
    list_filter = ('platform', 'genre', 'comment')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'games')
    search_fields = ('name','games')
    
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'games')
    search_fields = ('name', 'games')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'body', 'gameID', 'replies')
    search_fields = ('name', 'body', 'gameID')

admin.site.register(Game, GameAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Comment, CommentAdmin)