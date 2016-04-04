# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_q_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='q_number',
            name='number',
            field=models.CharField(max_length=50, verbose_name=b'number od displayed questions'),
        ),
    ]
