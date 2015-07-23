# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField()),
                ('posted', models.DateField(db_index=True, auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(to='blog.Category'),
        ),
    ]
