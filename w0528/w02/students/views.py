from django.shortcuts import render
from students.models import Student

# Create your views here.
def list(request):
   qs=Student.objects.order_by('-id') # 순차정렬
   context={'list':qs,'count':100,'id':'aaa'} # 딕셔너리 타입으로 전달
   return render(request,'students/list.html',context)

def view(request):
   name=request.GET.get('name')
   qs=Student.objects.get(name=name)
   context={'stu':qs}
   return render(request,'students/view.html',context)
   
def update(request,name):
   if request.method=='GET':
      qs=Student.objects.get(name=name)
      context={'stu':qs}
      return render(request,'students/update.html',context)
   else: 
      name2=request.POST.get('name')
      name2=request.POST.get('name')
      name2=request.POST.get('name')
      name2=request.POST.get('name')
      name2=request.POST.get('name')
   
def delete():