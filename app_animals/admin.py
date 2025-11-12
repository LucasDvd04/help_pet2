from django.contrib import admin
from .models import Animal,Location, PictureGalery,Comment


class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'uf',)
    search_fields = ('city', 'state', 'uf')

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'specie','dt_update',)
    list_filter = ('specie', 'gender')
    search_fields = ('name', 'specie__common_name')

class PictureAdmin(admin.ModelAdmin):
    list_display = ('picture','dt_insert',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'dt_create', 'dt_update', 'animal',)
    search_fields = ('content', 'animal__name',)


admin.site.register(Location, LocationAdmin),
admin.site.register(Animal, AnimalAdmin),
admin.site.register(PictureGalery, PictureAdmin),
admin.site.register(Comment, CommentAdmin),
