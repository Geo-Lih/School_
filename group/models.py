import datetime
from datetime import timezone

from django.db import models
# flake8: noqa
from students.models import Student
from teacher.models import Teacher


class Group(models.Model):
    student = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    id = models.BigAutoField
    group_name = models.CharField(max_length=64)
    group_direction = models.CharField(max_length=64)
    group_size = models.PositiveSmallIntegerField()

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

    @property
    def full_name(self):
        return f'{self.group_name} {self.group_direction} {self.group_size} in it'

    def get_full_info(self):
        return f'{self.id}{self.group_name} {self.group_direction},' \
               f' group_size={self.group_size}'
