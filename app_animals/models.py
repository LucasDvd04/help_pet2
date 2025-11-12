from django.db import models

# Create your models here.
class Location(models.Model):
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.city} - {self.uf}"

class Animal(models.Model):
    
    GENDER_CHOICES = [
        ('M','Macho'),
        ('F','Femea'),
    ]

    STATUS_CHOICES = [
        ('desaparecido', 'Desaparecido'),
        ('abandonado', 'Abandonado'),
        ('doação', 'Doação'),
    ]

    ESPECIE_CHOICES = [
        ('D','Dog'),
        ('C','Cat'),
        ('O','Other'),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    specie = models.CharField(max_length=1, choices=ESPECIE_CHOICES, default='D')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='desaparecido')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='animal_location', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def first_picture(self):
        """Retorna a primeira foto do animal, se existir."""
        first = self.picture_animal.first()
        return first.picture.url if first else None
    
class PictureGalery(models.Model):
    picture = models.ImageField(upload_to='animal_pictures/')
    dt_insert = models.DateTimeField(auto_now_add=True)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, related_name='picture_animal', null=True, blank=True)

class Comment(models.Model):
    content = models.TextField(max_length=300)
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, related_name='comment_animal', null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content