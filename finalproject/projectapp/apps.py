from django.apps import AppConfig


class ProjectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projectapp'

    # when app is ready, import signals
    def read(self):
        import projectapp.signals
