# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from noema_site.creater.menu import create_menus

class Migration(migrations.Migration):

    dependencies = [
        ('noema_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_menus)
    ]
