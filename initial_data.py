import os
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "es_project.settings")
django.setup()

call_command('loaddata', 'sex', app_label='dashboard')

