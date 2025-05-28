from django.shortcuts import render
from stuscore.models import Stuscore

def score(request):
   qs = Stuscore.objects.all()
   context = {'score':qs}
   return render(request,'score.html',context)