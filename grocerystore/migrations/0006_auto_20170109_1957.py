# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 03:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocerystore', '0005_auto_20170109_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='product_brand_variety',
            new_name='product_brand_or_variety',
        ),
    ]
