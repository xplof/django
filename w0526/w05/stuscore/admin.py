from django.contrib import admin
from stuscore.models import Stuscore

class StuscoreAdmin(admin.ModelAdmin):
   list_display=['no','name','total']
   

admin.site.register(Stuscore,StuscoreAdmin)

# Register your models here.
