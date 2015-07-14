# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('links', '0002_link_submitted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='boosters',
            field=models.ManyToManyField(related_name='boosted_links', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='link',
            name='score',
            field=models.SmallIntegerField(default=0),
        ),
    ]
