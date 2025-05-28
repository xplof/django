from django.db import models
import datetime

# Create your models here.
class Event(models.Model):
   no=models.AutoField(primary_key=True)
   title=models.CharField()
   startdate=models.DateField()
   enddate=models.DateField()
   rdate=models.DateField(default=datetime)