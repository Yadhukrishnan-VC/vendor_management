from django.apps import AppConfig

class PerfomanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfomance'
    
    def ready(self):
        import perfomance.receivers
