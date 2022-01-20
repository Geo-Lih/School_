from django.db import models
# flake8: noqa
from students.validator import validate_phone
from teacher.models import Teacher


class Student(models.Model):
    teachers = models.ManyToManyField(Teacher)
    id = models.BigAutoField
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    phone = models.CharField(
        max_length=13,
        validators=[validate_phone]
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_info(self):
        return f'{self.id}{self.first_name} {self.last_name}, age={self.age}'


class Logger(models.Model):
    method = models.CharField(max_length=12)
    path = models.URLField(max_length=666)
    execution_time = models.FloatField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.email
