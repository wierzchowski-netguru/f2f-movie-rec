from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f'[{self.__class__.__name__}] {self.username}'


class Movie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'[{self.__class__.__name__}] {self.name}'


class Rating(models.Model):
    user = models.ForeignKey('app.User', on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey('app.Movie', on_delete=models.CASCADE, related_name='ratings')

    rating = models.IntegerField(choices=((x, x) for x in range(1, 6)))

    def __str__(self):
        return f'[{self.__class__.__name__}] {self.user.username} {self.movie.name}'
