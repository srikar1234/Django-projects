from django.apps import AppConfig

#Add class name in main project inside settings.py folder
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
