# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0009_auto_20180207_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='content',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='first_section',
        ),
        migrations.RemoveField(
            model_name='chaptersection',
            name='next_section',
        ),
        migrations.RemoveField(
            model_name='chaptersection',
            name='previous_section',
        ),
        migrations.AddField(
            model_name='chaptersection',
            name='chapter',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='chapter_section', to='chapters.Chapter'),
            preserve_default=False,
        ),
    ]
