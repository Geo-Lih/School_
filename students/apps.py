from django.apps import AppConfig
# flake8: noqa


class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'

    def ready(self):
        from students import signals
