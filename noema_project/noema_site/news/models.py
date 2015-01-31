__author__ = 'master'

from django.db.models import (Model, AutoField,
                              TextField, ForeignKey)

from noema_project.noema_site.menu.models import MenuItem


class Message(Model):
    id = AutoField(primary_key=True)
    menu_item = ForeignKey(MenuItem, null=False, blank=False)
    content = TextField(default='', blank=True, null=False)

    class Meta:
        db_table = 'message'