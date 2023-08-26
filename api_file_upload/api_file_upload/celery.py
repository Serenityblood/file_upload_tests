import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_file_upload.settings")
app = Celery("api_file_upload")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'Testing new files': {
        'task': 'api.tasks.check_files',
        'schedule': 10
    },
}
app.conf.timezone = 'UTC'
