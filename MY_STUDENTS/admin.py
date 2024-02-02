from django.contrib import admin
from MY_STUDENTS.models import *
# Register your models here.
@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    # list_display=["idno","img","name","age","rollno","class_name","mobile","email","password"]
    list_display=[field.name for field in Student._meta.fields]
