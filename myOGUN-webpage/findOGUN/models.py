from __future__ import unicode_literals

from django.db import models


class Ogun(models.Model):
    id = models.IntegerField(primary_key=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    ects = models.IntegerField(blank=True, null=True)
    adress = models.CharField(max_length=255, blank=True, null=True)
    hours_number = models.IntegerField(blank=True, null=True)
    date_of_lessons = models.CharField(max_length=255, blank=True, null=True)
    ogun_group_id = models.CharField(max_length=255)
    date_week_day = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ogun'
