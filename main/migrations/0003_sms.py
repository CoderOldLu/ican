# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('mobile', models.CharField(max_length=11)),
                ('message', models.CharField(max_length=100)),
                ('sendTime', models.DateTimeField()),
            ],
            options={
                'ordering': ['-sendTime'],
            },
        ),
    ]
