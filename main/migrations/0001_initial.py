# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('caption', models.CharField(unique=True, max_length=50, verbose_name='标签名称')),
            ],
            options={
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('caption', models.CharField(max_length=100, verbose_name='名称')),
                ('cover', models.ImageField(upload_to=main.models.cover_upload_to, verbose_name='封面')),
                ('showcase', models.ImageField(blank=True, upload_to=main.models.showcase_upload_to, verbose_name='横幅')),
                ('intro', models.TextField(verbose_name='简介')),
                ('intro1', models.TextField(verbose_name='摘要')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('length', models.CharField(blank=True, max_length=20, verbose_name='总时长')),
                ('homepage', models.BooleanField(default=False, verbose_name='放到首页？')),
            ],
            options={
                'verbose_name_plural': '课程',
                'verbose_name': '课程',
            },
        ),
        migrations.CreateModel(
            name='TutorialCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('caption', models.CharField(max_length=20, verbose_name='名称')),
            ],
            options={
                'verbose_name_plural': '课程类别',
                'verbose_name': '课程类别',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('caption', models.CharField(max_length=200, verbose_name='标题')),
                ('length', models.CharField(max_length=20, verbose_name='时长')),
                ('file', models.FileField(upload_to=main.models.video_upload_to, verbose_name='视频文件')),
                ('tags', models.ManyToManyField(to='main.Tag', verbose_name='标签')),
                ('tutorial', models.ForeignKey(to='main.Tutorial', verbose_name='课程')),
            ],
            options={
                'verbose_name_plural': '视频',
                'verbose_name': '视频',
            },
        ),
        migrations.AddField(
            model_name='tutorial',
            name='category',
            field=models.ForeignKey(to='main.TutorialCategory', verbose_name='课程类别'),
        ),
    ]
