from django.db import models

# db 연결 - 컬럼 : 이름 과목 등급 나이 성별

class Student(models.Model):
   name=models.CharField(max_length=100)
   major=models.CharField(max_length=100)
   grade=models.IntegerField(default=0)
   age=models.IntegerField(default=0)
   gender=models.CharField(max_length=100)
   
   def __str__(self):
      return f'{self.name},{self.age}'
   
