from django.db import models

# Create your models here.

class BillTracker(models.Model):
    expenseType = models.TextField()
    amount = models.IntegerField()
    date = models.DateField()

def __str__(self):
    return '%s %s %s' % (self.expenseType, self.amount, self.date)