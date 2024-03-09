from django.db import models

# Model representing movie genres
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model representing actors
class Actor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Model representing movies
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)  # Many-to-many relationship with Genre model
    actors = models.ManyToManyField(Actor)  # Many-to-many relationship with Actor model

    def __str__(self):
        return self.title

# Model representing user ratings for movies
class Rating(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Foreign key to Django's built-in User model
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Foreign key to Movie model
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # Decimal field to store ratings

    def __str__(self):
        return f"{self.user.username} rated {self.movie.title} {self.rating}"
