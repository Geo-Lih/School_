from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import Student


@receiver(pre_save, sender=Student)
def capitalize_name(instance, **kwargs):
    print('Works')
    first_name = instance.first_name
    last_name = instance.last_name
    instance.first_name = str.capitalize(first_name)
    instance.last_name = str.capitalize(last_name)
