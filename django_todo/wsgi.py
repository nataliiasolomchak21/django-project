# The comments at the top explain this is the WSGI config for the django_todo project.
# WSGI (Web Server Gateway Interface) helps deploy Django to web servers.
"""
WSGI config for django_todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
# We import os and get_wsgi_application from django.
import os
# os.environ sets the DJANGO_SETTINGS_MODULE environment variable to point to the project's settings.
# This tells Django which settings file to use for this application.
from django.core.wsgi import get_wsgi_application
# get_wsgi_application returns a WSGI callable application. A callable is something that can be called.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')
# The application callable can be served by WSGI compatible web servers.
application = get_wsgi_application()
