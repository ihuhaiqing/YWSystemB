from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task(bind=True)
def debug_task(self):
    return f'Hello Celery, the task id is: {self.request.id}'
