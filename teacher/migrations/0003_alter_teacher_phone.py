# Generated by Django 3.2.9 on 2021-12-25 20:46

from django.db import migrations, models
import students.validator


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=13, validators=[students.validator.validate_phone]),
        ),
    ]
