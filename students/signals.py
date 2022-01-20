from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from students.models import Student

from students.models import Contact
from .tasks import send_email


@receiver(pre_save, sender=Student)
def capitalize_name(instance, **kwargs):
    print('Works')
    first_name = instance.first_name
    last_name = instance.last_name
    instance.first_name = str.capitalize(first_name)
    instance.last_name = str.capitalize(last_name)


@receiver(post_save, sender=Contact)
def email_signal(sender, instance, **kwargs):
    context = {
        'email': instance.email,
        'message': instance.message,
    }
    send_email.delay(**context)
