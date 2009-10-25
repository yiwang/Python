from django.conf.urls.defaults import *
#from mysite.moneysim.models import Poll

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'mysite.moneysim.views.index'),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
