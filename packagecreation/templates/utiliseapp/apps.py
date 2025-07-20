from django.apps import AppConfig


class UtiliseappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utiliseapp'

from django.apps import AppConfig

class {{ app_name|capfirst }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ app_name }}'
