from django.shortcuts import render

# Create your views here.
def list(req):
   return render(req,'event/list.html')