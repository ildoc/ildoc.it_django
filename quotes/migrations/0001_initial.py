# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name=b'Testo')),
                ('author', models.CharField(max_length=200, verbose_name=b'Autore')),
                ('url', models.CharField(max_length=200, verbose_name=b'Url', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
