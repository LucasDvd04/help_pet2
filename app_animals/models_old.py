
#     from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class Species(models.Model):
#     common_name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.common_name


# class Location(models.Model):
#     state = models.CharField(max_length=30)
#     city = models.CharField(max_length=30)
#     uf = models.CharField(max_length=2)

#     def __str__(self):
#         return f"{self.city} - {self.uf}"


# class Animal(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Macho'),
#         ('F', 'Fêmea'),
#         ('U', 'Indefinido'),
#     ]

#     STATUS_CHOICES = [
#         ('disponivel', 'Disponível'),
#         ('adotado', 'Adotado'),
#         ('resgatado', 'Resgatado'),
#     ]


#     name = models.CharField(max_length=100, null=True, blank=True)
#     age = models.IntegerField(null=True, blank=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
#     specie = models.ForeignKey(Species, on_delete=models.PROTECT, related_name='animals')
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
#     location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='animals', null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     dt_create = models.DateTimeField(auto_now_add=True)
#     dt_update = models.DateTimeField(auto_now=True)

#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animals')  # quem cadastrou
#     likes = models.ManyToManyField(User, related_name='liked_animals', blank=True)

#     def __str__(self):
#         return self.name or "Animal sem nome"

#     def total_likes(self):
#         return self.likes.count()


# class AnimalPicture(models.Model):
#     """Tabela para armazenar várias imagens de um mesmo animal."""
#     animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='pictures')
#     picture = models.ImageField(upload_to='animal_pictures/', null=True, blank=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Foto de {self.animal.name or 'Animal'}"


# class Comment(models.Model):
#     animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Comentário de {self.user.username} em {self.animal.name}'

    
