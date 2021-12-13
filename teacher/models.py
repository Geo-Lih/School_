from django.db import models
# flake8: noqa

class Teacher(models.Model):
    id = models.BigAutoField
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.age}y.o.'
