import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HealthCareProject.settings')

# Create an instance of the Celery app
app = Celery('HealthCareProject')

# Load the Celery configuration from the Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover and register your Django app tasks
app.autodiscover_tasks()
