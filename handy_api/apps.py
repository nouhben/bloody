from django.apps import AppConfig


class HandyApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'handy_api'

    def ready(self):
        import handy_api.signals
