# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-08-13 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0004_auto_20180813_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communitymember',
            options={'permissions': (('ban_member', 'Can ban members'),)},
        ),
    ]
