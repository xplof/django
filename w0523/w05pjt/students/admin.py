from django.contrib import admin
from students.models import Student
# Register your models here.

#어드민 관리자 페이지 등록
admin.site.register(Student)