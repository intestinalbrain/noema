# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_menus(apps, schema_editor):
    noema_menu_schema = {'news': {'name': u'Новости',
                                  'parent': None},
                         'poster': {'name': u'Постер',
                                    'parent': 'news'},
                         'gallery': {'name': u'Галерея',
                                     'parent': 'news'},
                         'discography': {'name': u'Дискография',
                                         'parent': 'news'},
                         'band': {'name': u'О группе',
                                  'parent': None}}

    Menu = apps.get_model('noema_site', 'Menu')
    menu = Menu(code='noema', name='noema')
    menu.save()

    menu_id = menu.id

    item_code_list = []

    for code, attrs in noema_menu_schema.items():




class Migration(migrations.Migration):

    dependencies = [
        ('noema_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_menus),
    ]
