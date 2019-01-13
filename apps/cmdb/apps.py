from django.apps import AppConfig


class CmdbConfig(AppConfig):
    name = 'cmdb'

    def ready(self):
        from .signals import auto_delete_connection
        from .signals import auto_delete_file
        from .signals import auto_compare_diff
