from django.conf.urls import patterns, include, url
from django.contrib import admin

from noema_site.band.views import view_band
from noema_site.news.views import view_news, view_one_news
from noema_site.news.discography.views import view_discography
from noema_site.news.gallery.views import view_gallery
from noema_site.news.poster.views import view_poster

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noema_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', view_news, name='home'),
    url(r'^home$', view_news, name='home'),
    url(r'^news$', view_news, name='news'),
    url(r'^news/(?P<news_id>\d+)$', view_one_news, name='one_news'),
    url(r'^band$', view_band, name='band'),
    url(r'^discography$', view_discography, name='discography'),
    url(r'^gallery$', view_gallery, name='gallery'),
    url(r'^poster$', view_poster, name='poster'),
    url(r'^admin/', include(admin.site.urls)),
    )
