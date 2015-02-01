# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'menu',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=32)),
                ('menu', models.ForeignKey(default=None, blank=True, to='noema_site.Menu', null=True)),
                ('parent', models.ForeignKey(default=None, blank=True, to='noema_site.MenuItem', null=True)),
            ],
            options={
                'db_table': 'menu_item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('menu_item', models.ForeignKey(to='noema_site.MenuItem')),
            ],
            options={
                'db_table': 'news',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.TextField(default=b'', blank=True)),
                ('is_preview', models.BooleanField(default=False)),
                ('news', models.ForeignKey(to='noema_site.NewsItem')),
            ],
            options={
                'db_table': 'news_item',
            },
            bases=(models.Model,),
        ),
    ]
