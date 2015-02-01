__author__ = 'master'

from django.db.models import (Model, AutoField, CharField,
                              TextField, ForeignKey, BooleanField)

from noema_site.menu.models import MenuItem

class News(Model):
    id = AutoField(primary_key=True)
    menu_item = ForeignKey(MenuItem, null=False, blank=False)
    title = CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'news'

    def context(self):
        for news_item in NewsItem.objects.filter(news=self):
            pass



class NewsItem(Model):
    id = AutoField(primary_key=True)
    content = TextField(default='', blank=True, null=False)
    news = ForeignKey('self', null=False, blank=False)
    is_preview = BooleanField(null=False, default=False, blank=True)

    class Meta:
        db_table = 'news_item'