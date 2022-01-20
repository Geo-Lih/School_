from django.db import models
# flake8: noqa
from students.models import Student
from teacher.models import Teacher


class Group(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    id = models.BigAutoField
    group_name = models.CharField(max_length=64)
    group_direction = models.CharField(max_length=64)
    group_size = models.PositiveSmallIntegerField()

    @property
    def full_name(self):
        return f'{self.group_name} {self.group_direction} {self.group_size} in it'

    def get_full_info(self):
        return f'{self.id}{self.group_name} {self.group_direction},' \
               f' group_size={self.group_size}'
