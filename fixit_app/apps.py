from django.apps import AppConfig


class FixitAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fixit_app"

def ready(self):
    import fixit_app.signals