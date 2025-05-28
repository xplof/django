from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from students.models import Student
from django.urls import reverse

# Create your views here.
def list(request):
   return render(request,'students/list.html')


def write(request):
   return render(request,'students/write.html')

def write2(request):
   name=request.POST.get('name')
   major=request.POST.get('major')
   grade=request.POST.get('grade')
   age=request.POST.get('age')
   gender=request.POST.get('gender')
   
   qs=Student(name=name,major=major,age=age,grade=grade,gender=gender)
   qs.save()
   
   return HttpResponse('등록후 메인페이지로 이동')
   # return render(request,'students/write.html')



