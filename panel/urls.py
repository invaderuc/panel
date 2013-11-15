from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','solar.views.index'),
    url(r'^nosotros/$','solar.views.nosotros'),
    url(r'^mas/$','solar.views.mas'),
    url(r'^laenergiasolar/$','solar.views.laenergiasolar'),
    url(r'^limitaciones/$','solar.views.limitaciones'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)