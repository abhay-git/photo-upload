# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_document_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
    ]