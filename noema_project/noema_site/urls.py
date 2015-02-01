# coding: utf-8

from django.conf.urls import patterns, url

from news.views import view_news, view_one_news

urlpatterns = patterns('',
    url(r'home^$', view_news, name='home'),
    url(r'news^$', view_news, name='news'),
    url(r'^new/(?P<question_id>\d+)$', view_one_news, name='one_news'),
    )
