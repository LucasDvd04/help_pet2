from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from .models import Animal

# @receiver(post_save, sender=Animal)
# def animal_post_save(sender, instance, **kwargs):
#     print('### Post save animal ###')
#     print(instance.id)