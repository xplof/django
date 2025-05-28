from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from students.models import Student

#학생정보 삭제
def delete(request,name):
   qs=Student.objects.get(name=name)
   qs.delete()
   return redirect('/students/list')

#학생정보 수정
def update(request,name):
   if request.method=='GET':
      qs=Student.objects.get(name=name)#해당 정보 검색
      context={'stu':qs}
      return render(request,'students/update.html',context)
   else:
      name2= request.POST.get('name')
      major = request.POST.get('major')
      grade = request.POST.get('grade')
      age = request.POST.get('age')
      gender = request.POST.get('gender')
      # db수정
      
      # 1. 회원검색
      qs=Student.objects.get(name=name)
      # 2. 회원정보수정
      qs.name=name2
      qs.major=major
      qs.grade=grade
      qs.age=age
      qs.gender=gender
      # 3. 저장
      qs.save()
      return redirect('/students/list')
   
# 상세보기
def view(request):
   name=request.GET.get('name')
   qs=Student.objects.get(name=name)
   context={'stu':qs}
   return render(request,'students/view.html',context)

#학생정보 등록
def write(request):
   if request.method=='POST':
      name = request.POST.get('name')
      major = request.POST.get('major')
      grade = request.POST.get('grade')
      age = request.POST.get('age')
      gender = request.POST.get('gender')
      
      Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
      
      return redirect('/students/list')
   else: #GET방식으로 들어올때

      return render(request,'students/write.html')
   
#학생정보 리스트
def list(request):
      #DB 검색 objects.all():전체가져오기 objects.get(): 해당되는것 가져오기
      #objects.filter() 검색기눙
   # qs=Student.objects.all() #전체 가져오기
   qs=Student.objects.order_by('-id') # 순차정렬
   context={'list':qs,'count':100,'id':'aaa'} # 딕셔너리 타입으로 전달
   return render(request,'students/list.html',context)