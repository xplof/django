from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list(request):
   return render(request,'list.html')
   # return HttpResponse('리스트페이지 연결')