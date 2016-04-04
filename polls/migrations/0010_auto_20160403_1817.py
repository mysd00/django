# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20160325_1959'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Q_number',
        ),
        migrations.RemoveField(
            model_name='question1',
            name='category',
        ),
        migrations.RemoveField(
            model_name='question1',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, to='polls.Category', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.TextField(help_text=b'if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default=b'text', max_length=200, choices=[(b'text', b'text'), (b'radio', b'radio'), (b'select', b'select'), (b'select-multiple', b'Select Multiple'), (b'integer', b'integer')]),
        ),
        migrations.AddField(
            model_name='question',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(default=True, to='polls.Survey'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=datetime.datetime(2016, 4, 3, 16, 17, 17, 868000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Question1',
        ),
    ]
