from django.db import models

# Create your models here.
class Student(models.Model):
   no=models.AutoField(primary_key=True)
   name=models.CharField()
   grade=models.IntegerField()
   age=models.IntegerField()
   gender=models.CharField()
   
   def __str__(self):
      return f'{self.name},{self.age}'