import os

from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fabZ.settings')

app = Celery(
    'backend',
    broker='redis://redis'
)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_url = 'redis://127.0.0.1:6379/0'

app.conf.timezone = 'UTC'

app.autodiscover_tasks()

