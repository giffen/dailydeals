from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		(r'^accounts/', include('registration.backends.default.urls')),
		url(r'^$', 'dailydeals.views.home', name='home'),
		url(r'^contact/$', 'contact.views.contact', name='contact_us'),
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^deals/$', 'deals.views.all_deals'),
    url(r'^deals/(?P<year>\d{4})/$', 'deals.views.year_archive'),
    url(r'^deals/(?P<year>\d{4})/(?P<month>\d{2})/$', 'deals.views.month_archive'),
    url(r'^deals/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>.*)/$',
	    		 'deals.views.deal_detail', 
	    		 	name='deal_detail'),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)