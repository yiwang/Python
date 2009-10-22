from django.conf.urls.defaults import *
from mysite.polls.models import Poll

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

info_dict = {
    'queryset': Poll.objects.all(),
}

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='polls/results.html'), 'poll_results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'mysite.polls.views.vote'),


    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
