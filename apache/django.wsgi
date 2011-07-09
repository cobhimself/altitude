import os, sys

path = '/home/administrator/django_projects'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'altitude.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
