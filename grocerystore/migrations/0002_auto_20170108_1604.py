# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerystore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('store_city', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(default=None, upload_to=b''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_store',
            field=models.ManyToManyField(to='grocerystore.Store'),
        ),
    ]
