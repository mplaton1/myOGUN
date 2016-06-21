# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Ogun(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    link = models.TextField(blank=True, null=True)  # This field type is a guess.
    ects = models.IntegerField(blank=True, null=True)
    adress = models.TextField(blank=True, null=True)  # This field type is a guess.
    hours_number = models.IntegerField(blank=True, null=True)
    date_of_lessons = models.TextField(blank=True, null=True)  # This field type is a guess.
    ogun_group_id = models.TextField()  # This field type is a guess.
    date_week_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_time = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_time = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'ogun'
