from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name'] #orders movies alphabetically
    search_fields = ['name'] #lets you search by name

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)