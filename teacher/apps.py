from django.apps import AppConfig
# flake8: noqa


class TeacherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teacher'

    def ready(self):
        from teacher import signals
