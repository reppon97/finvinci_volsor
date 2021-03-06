from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "volsor.settings")

# Setting up celery.
app = Celery("volsor")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
