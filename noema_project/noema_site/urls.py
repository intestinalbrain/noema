# # coding: utf-8
#
# from django.conf.urls import patterns, url
#
# from band.views import view_band
# from news.views import view_news, view_one_news
# from news.discography.views import view_discography
# from news.gallery.views import view_gallery
# from news.poster.views import view_poster
#
#
# urlpatterns = patterns('',
#     url(r'home^$', view_news, name='home'),
#     url(r'news^$', view_news, name='news'),
#     url(r'^news/(?P<news_id>\d+)$', view_one_news, name='one_news'),
#     url(r'band^$', view_band, name='band'),
#     url(r'discography^$', view_discography, name='discography'),
#     url(r'gallery^$', view_gallery, name='gallery'),
#     url(r'poster^$', view_poster, name='poster'),
#     )
