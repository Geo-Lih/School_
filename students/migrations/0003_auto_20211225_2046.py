# Generated by Django 3.2.9 on 2021-12-25 20:46
# flake8: noqa
from django.db import migrations, models
import students.validator


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=12)),
                ('path', models.URLField(max_length=666)),
                ('execution_time', models.FloatField(max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=13, validators=[students.validator.validate_phone]),
        ),
    ]
