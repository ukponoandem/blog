from django.db import models
from datetime import datetime

# Create your models here.
class blogs(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=100000000)
    current_date = models.DateTimeField(default=datetime.now,blank=True)