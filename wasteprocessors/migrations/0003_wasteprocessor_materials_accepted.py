# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasteprocessors', '0002_auto_20160427_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='wasteprocessor',
            name='materials_accepted',
            field=models.ManyToManyField(related_name='material_types', to='wasteprocessors.MaterialType'),
        ),
    ]
