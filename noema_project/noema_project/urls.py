from django.conf.urls import patterns, include, url
from django.contrib import admin

import noema_project

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noema_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(noema_project.noemo_site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    )
