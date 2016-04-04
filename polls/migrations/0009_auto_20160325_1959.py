# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_question1_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('interviewer', models.CharField(max_length=400, verbose_name=b'Name of Interviewer')),
                ('interviewee', models.CharField(max_length=400, verbose_name=b'Name of Interviewee')),
                ('conditions', models.TextField(null=True, verbose_name=b'Conditions during interview', blank=True)),
                ('comments', models.TextField(null=True, verbose_name=b'Any additional Comments', blank=True)),
                ('interview_uuid', models.CharField(max_length=36, verbose_name=b'Interview unique identifier')),
                ('survey', models.ForeignKey(to='polls.Survey')),
            ],
        ),
        migrations.AlterField(
            model_name='question1',
            name='choices',
            field=models.TextField(help_text=b'if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .', null=True, blank=True),
        ),
        migrations.CreateModel(
            name='AnswerInteger',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.AnswerBase')),
                ('body', models.IntegerField(null=True, blank=True)),
            ],
            bases=('polls.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerRadio',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.AnswerBase')),
                ('body', models.TextField(null=True, blank=True)),
            ],
            bases=('polls.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerSelect',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.AnswerBase')),
                ('body', models.TextField(null=True, blank=True)),
            ],
            bases=('polls.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerSelectMultiple',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.AnswerBase')),
                ('body', models.TextField(null=True, blank=True)),
            ],
            bases=('polls.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerText',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.AnswerBase')),
                ('body', models.TextField(null=True, blank=True)),
            ],
            bases=('polls.answerbase',),
        ),
        migrations.AddField(
            model_name='answerbase',
            name='question',
            field=models.ForeignKey(to='polls.Question'),
        ),
        migrations.AddField(
            model_name='answerbase',
            name='response',
            field=models.ForeignKey(to='polls.Response'),
        ),
    ]
