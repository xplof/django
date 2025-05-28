from django.db import models


# ORM : Object Relational Mapping
#class객체 등록하면 db자동생성
# Create your models here.
class Student(models.Model):
   name=models.CharField(max_length=100)
   major=models.CharField(max_length=100)
   age=models.IntegerField(default=0)
   grade=models.IntegerField(default=0)
   gender=models.CharField(max_length=10)
   
   def __str__(self):
      return self.name
