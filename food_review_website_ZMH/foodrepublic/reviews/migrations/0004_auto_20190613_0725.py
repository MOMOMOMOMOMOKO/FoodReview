# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20190613_0722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='wine',
            new_name='food',
        ),
    ]
