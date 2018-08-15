# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=200)),
                ('description', models.CharField(verbose_name='描述', max_length=200)),
                ('cover', models.ImageField(verbose_name='图片', upload_to=main.models.slide_upload_to)),
                ('link', models.OneToOneField(verbose_name='链接到', to='main.Tutorial')),
            ],
            options={
                'verbose_name': '走马灯',
                'verbose_name_plural': '走马灯',
            },
        ),
    ]
