# Generated by Django 3.2.9 on 2022-01-20 14:37

from django.db import migrations, models
import django.db.models.deletion
# flake8: noqa


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_teacher_phone'),
        ('students', '0003_auto_20211225_2046'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
    ]
