# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20160325_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='question1',
            name='choices',
            field=models.TextField(help_text=b'if the question type is "Radio,""select",or"select multiple" provide a comma-separated list of options for this question.', blank=True),
        ),
    ]
