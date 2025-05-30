from django.db import models

# Create your models here.
class Member(models.Model):
   # 중복x, nullx - primary key(유일한 키)
   id=models.CharField(max_length=50,primary_key=True)
   pw=models.CharField()
   name=models.CharField()
   nickname=models.CharField()
   tel=models.CharField(default='010-0000-0000')
   gender=models.CharField(default='남자')
   hobby=models.CharField(default='게임')
   mdate=models.DateTimeField(auto_now=True,null=True)
   
   def __str__(self):
      return f'{self.id},{self.name},{self.nickname}'