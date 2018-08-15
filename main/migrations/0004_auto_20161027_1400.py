# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_sms'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['order_by'], 'verbose_name': '视频', 'verbose_name_plural': '视频'},
        ),
        migrations.AddField(
            model_name='video',
            name='order_by',
            field=models.IntegerField(default=0, verbose_name='顺序'),
        ),
    ]
