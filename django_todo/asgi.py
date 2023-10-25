# This docstring at the top provides some explanation about what the file is for - it is the ASGI config for a project called django_todo.
"""
ASGI config for django_todo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# Here we import the needed os module and get_asgi_application function from Django.
import os

from django.core.asgi import get_asgi_application

# This line sets the DJANGO_SETTINGS_MODULE environment variable to point to the project's settings file. This tells Django which settings to use for this ASGI application.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_todo.settings")
# We call get_asgi_application which returns a callable ASGI application based on the project's Django settings. This application callable can then be used by an ASGI web server.
application = get_asgi_application()
