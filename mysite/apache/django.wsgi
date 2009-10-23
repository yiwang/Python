import os
import sys
import django.core.handlers.wsgi

sys.path.append('/home/e/Desktop/Python')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
application = django.core.handlers.wsgi.WSGIHandler()


