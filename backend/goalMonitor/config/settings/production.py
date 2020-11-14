"""
Production settings for the goalMonitor project
"""
from .base import *
import os

# Allowed hosts for the production environment
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Static files and Media settings
STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
