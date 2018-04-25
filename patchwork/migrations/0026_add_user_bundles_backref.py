# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-12 11:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patchwork', '0025_add_regex_validators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundles', related_query_name='bundle', to=settings.AUTH_USER_MODEL),
        ),
    ]