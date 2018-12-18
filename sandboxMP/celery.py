# @Time   : 2018/12/9 20:50
# @Author : RobbieHan
# @File   : celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sandboxMP.settings')

app = Celery('sandbox')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

BROKER_URL = 'redis://localhost:6379/1'

CELERYD_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_ENABLE_UTC = False

CELERYD_FORCE_EXECV = True

CELERYD_CONCURRENCY = 5

CELERY_ACKS_LATE = True

CELERYD_MAX_TASKS_PER_CHILD = 100

CELERYD_TASK_TIME_LIMIT = 10 * 30

app.conf.ONCE = {
    'backend': 'celery_once.backends.Redis',
    'settings': {
        'url': 'redis://localhost:6379/3',
        'default_timeout': 10 * 30
    }
}

from datetime import timedelta

# CELERYBEAT_SCHEDULE = {
#     'task1': {
#         'task': 'sandbox_add',
#         'schedule': timedelta(seconds=5),
#         'args': (2, 8)
#     },
#
# }

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
