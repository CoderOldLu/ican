# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_commodity_trade_bill_user_buy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.CharField(max_length=300, verbose_name='视频文件'),
        ),
    ]
