# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20160320_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_else',
            field=models.CharField(default=2, max_length=200, verbose_name=b'question else'),
            preserve_default=False,
        ),
    ]
