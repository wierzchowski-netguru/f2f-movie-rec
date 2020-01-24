from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from app.models import Movie, Rating

User = get_user_model()


@admin.decorators.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.decorators.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.decorators.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'user', 'rating')
