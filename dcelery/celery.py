from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# import pdb; pdb.set_trace()
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dcelery.settings")

app = Celery("dcelery")
app.config_from_object("django.conf:settings",namespace="CELERY")
app.autodiscover_tasks()

app.conf.imports = ("tasks.tasks")


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
