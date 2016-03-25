# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_question_question_else'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Question1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('required', models.BooleanField()),
                ('question_type', models.CharField(default=b'text', max_length=200, choices=[(b'text', b'text'), (b'radio', b'radio'), (b'select', b'select'), (b'select-multiple', b'Select Multiple'), (b'integer', b'integer')])),
                ('category', models.ForeignKey(blank=True, to='polls.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_else',
        ),
        migrations.AlterField(
            model_name='q_number',
            name='number',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='question1',
            name='survey',
            field=models.ForeignKey(to='polls.Survey'),
        ),
        migrations.AddField(
            model_name='category',
            name='survey',
            field=models.ForeignKey(to='polls.Survey'),
        ),
    ]
