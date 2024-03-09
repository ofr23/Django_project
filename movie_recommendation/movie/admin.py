from django.contrib import admin
from .models import Genre, Actor, Movie, Rating

# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    filter_horizontal = ('genres', 'actors')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating')
