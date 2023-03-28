# comment/__init__.py
"""
Aplicativo Django para comentários.
"""

from django.apps import AppConfig

class CommentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'