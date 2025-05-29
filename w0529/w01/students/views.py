from django.shortcuts import render
from students.models import Student

# Create your views here.
def list(request):
   qs=Student.objects.order_by('id')
   context={'list':qs}
   return render(request,'students/list.html',context)