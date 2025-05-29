from django.db import models

# Create your models here.
class Student(models.Model):
   name=models.CharField()
   major=models.CharField()
   grade=models.IntegerField()
   age=models.IntegerField()
   gender=models.CharField()
   
   def __str__(self):
      return self.name
   