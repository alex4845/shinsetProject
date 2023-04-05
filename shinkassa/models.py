from datetime import datetime

from django.db import models

class Worktable(models.Model):
    company = models.CharField(max_length=30, null=True, blank=True)
    vehicle = models.CharField(max_length=25, null=True, blank=True)
    number = models.CharField(max_length=15, null=True, blank=True)
    diametr = models.CharField(max_length=10)
    complex = models.IntegerField(max_length=3, default=0, null=True, blank=True)
    balance = models.IntegerField(max_length=3, null=True, blank=True, default=0)
    count_gruz = models.IntegerField(max_length=3, null=True, blank=True, default=0)
    sn = models.IntegerField(max_length=3, null=True, blank=True, default=0)
    ust = models.IntegerField(max_length=3, null=True, blank=True, default=0)
    mont = models.IntegerField(max_length=3, null=True, blank=True, default=0)
    demont = models.IntegerField(max_length=3, null=True, blank=True, default=0)
    appworks = models.CharField(max_length=50, null=True, blank=True)
    cost_appworks = models.FloatField(max_length=10, null=True, blank=True, default=0)
    time = models.CharField(max_length=20, blank=True, null=True)
    summ = models.FloatField(max_length=10, null=True, blank=True, default=0)

    def __str__(self):
        return self.diametr







