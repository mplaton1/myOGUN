# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ogun',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.TextField(blank=True, null=True)),
                ('ects', models.IntegerField(blank=True, null=True)),
                ('adress', models.TextField(blank=True, null=True)),
                ('hours_number', models.IntegerField(blank=True, null=True)),
                ('date_of_lessons', models.TextField(blank=True, null=True)),
                ('ogun_group_id', models.TextField()),
                ('date_week_day', models.TextField(blank=True, null=True)),
                ('start_time', models.TextField(blank=True, null=True)),
                ('end_time', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ogun',
            },
        ),
    ]
