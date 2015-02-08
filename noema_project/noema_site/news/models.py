__author__ = 'master'

from django.db.models import (Model, AutoField, CharField,
                              TextField, ForeignKey, BooleanField)

from noema_site.menu.models import MenuItem

from noema_site.context.context import ModelItemContext

class News(Model):
    id = AutoField(primary_key=True)
    menu_item = ForeignKey(MenuItem, null=False, blank=False)
    title = CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'news'

    def context(self, alias={}):
        return ModelItemContext(self).compile()



class NewsItem(Model):
    id = AutoField(primary_key=True)
    content = TextField(default='', blank=True, null=False)
    news = ForeignKey('self', null=False, blank=False)
    is_preview = BooleanField(null=False, default=False, blank=True)

    class Meta:
        db_table = 'news_item'