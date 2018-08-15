# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20161027_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='名称', max_length=100)),
                ('description', models.TextField(verbose_name='描述')),
                ('price', models.IntegerField(verbose_name='价格', blank=True)),
                ('days', models.IntegerField(verbose_name='有效期(天数)')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='Trade_bill',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=32, unique=True)),
                ('alipay_id', models.CharField(max_length=100, blank=True)),
                ('start', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('commodity', models.ForeignKey(to='main.Commodity')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_buy',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('expire', models.DateField()),
                ('price', models.FloatField(default=0)),
                ('order_id', models.CharField(max_length=64, blank=True, default='#')),
                ('alipay_id', models.CharField(max_length=100, blank=True, default='#')),
                ('payed', models.BooleanField(default=False)),
                ('commodity', models.ForeignKey(to='main.Commodity')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-expire'],
            },
        ),
    ]
