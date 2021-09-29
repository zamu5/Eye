"""
WSGI config for eye project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from events.thread import start_queue
import threading

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eye.settings')

application = get_wsgi_application()
threading.Thread(target=start_queue, daemon=True).start()