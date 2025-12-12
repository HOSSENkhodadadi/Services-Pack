from django.apps import AppConfig


class ServicesConfig(AppConfig):
    """
    Configuration for the services app.
    This is where all our service logic lives.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
