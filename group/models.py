from django.db import models
# flake8: noqa

class Group(models.Model):
    id = models.BigAutoField
    group_name = models.CharField(max_length=64)
    group_direction = models.CharField(max_length=64)
    group_size = models.PositiveSmallIntegerField()

    def get_full_info(self):
        return f'{self.id}{self.group_name} {self.group_direction},' \
               f' age={self.group_size}'
