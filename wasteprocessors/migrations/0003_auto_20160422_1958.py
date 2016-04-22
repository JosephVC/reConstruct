# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-22 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasteprocessors', '0002_auto_20160418_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waste',
            name='description',
        ),
        migrations.AlterField(
            model_name='wasteprocessor',
            name='materials_accepted',
            field=models.ManyToManyField(related_name='material_types', to='wasteprocessors.MaterialType'),
        ),
    ]