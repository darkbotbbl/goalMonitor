"""
Development settings for the goalMonitor project
"""
from .base import *
import os

# Allowed hosts on the development environment
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

STATIC_URL = "/static/"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'