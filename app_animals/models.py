from django.db import models

# Create your models here.

class Species(models.Model):
    common_name = models.CharField(max_length=30)

    def __str__(self):
        return self.common_name
    
class GenderChoices(models.Model):
    gender = models.CharField(max_length=30)

    def __str__(self):
        return self.gender

class Status(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status

class Location(models.Model):
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.city} - {self.uf}"

class Animal(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.ForeignKey(GenderChoices, on_delete=models.PROTECT, related_name='animal_gender')
    specie = models.ForeignKey(Species, on_delete=models.PROTECT, related_name='animal_species')
    picture = models.ImageField(upload_to='animal_pictures/', null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='animal_status')
    state = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='animal_location', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
