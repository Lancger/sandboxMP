import os

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sandboxMP.settings')

conf_file = os.path.join(os.path.join(settings.BASE_DIR, 'config'), 'host_scan.yml')

