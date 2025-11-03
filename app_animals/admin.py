from django.contrib import admin
from .models import Species, Animal, GenderChoices, Status, Location

class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('common_name',)
    search_fields = ('common_name',)

class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('status',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'uf')
    search_fields = ('city', 'state', 'uf')

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'specie')
    list_filter = ('specie', 'gender')
    search_fields = ('name', 'specie__common_name')


admin.site.register(Species, SpeciesAdmin),
admin.site.register(GenderChoices, GenderAdmin),
admin.site.register(Status, StatusAdmin),
admin.site.register(Location, LocationAdmin),
admin.site.register(Animal, AnimalAdmin),
