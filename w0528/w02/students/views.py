from django.shortcuts import render
from students.models import Student

# Create your views here.
def list(request):
   qs=Student.objects.order_by('-id') # 순차정렬
   context={'list':qs,'count':100,'id':'aaa'} # 딕셔너리 타입으로 전달
   return render(request,'students/list.html',context)

def list(request):
   qs=Student.objects.all()
   context={'list':qs}
   return render(request,'students/list.html')