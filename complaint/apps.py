from django.apps import AppConfig


class ComplaintConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'complaint'

    def ready(self):
        import complaint.signals
