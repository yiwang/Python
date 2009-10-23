from django.conf.urls.defaults import *
#from mysite.moneysim.models import Poll

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', 'mysite.moneysim.views.index'),


    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
