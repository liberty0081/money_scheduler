from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Outcome(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=25)
  date = models.DateField()
  price = models.IntegerField()
  note = models.TextField(max_length=200, blank=True)
  is_passed = models.BooleanField(default=False)