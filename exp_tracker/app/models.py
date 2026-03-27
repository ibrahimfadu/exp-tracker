from django.db import models

# Create your models here.

class Expense(models.Model):
    amount = models.CharField(max_length=200);

