
from datetime import date
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    estimated_end = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default=3)

    def __str__(self):
        return self.title