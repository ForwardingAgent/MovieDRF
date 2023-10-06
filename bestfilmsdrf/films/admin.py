from django.contrib import admin

from .models import Movie, Category

#admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'user', 'prop')


admin.site.register(Category)
