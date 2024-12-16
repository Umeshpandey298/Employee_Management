"""
WSGI config for emp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from employee import app as application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emp.settings')

application = get_wsgi_application()

app =application
