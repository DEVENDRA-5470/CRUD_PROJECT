from django.shortcuts import get_object_or_404, render
from MY_STUDENTS.forms import *
from django.contrib import messages
# Create your views here.
def home(request):
    info=Student.objects.all()
    return render(request,'home.html',{"info":info})

def account(request):
    if request.method=="POST":
        form=Student_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"SUCCESS ✔")
            return render(request,"success.html")
    form=Student_Form()
    return render(request,'regform.html',{'form':form})

def delete(request,id):
    if request.method == 'POST':
        student=Student.objects.get(pk=id)
        print(student,"--------------")
        student.delete()

    form=Student_Form()
    return render(request,'regform.html',{'form':form})

def update(request,id):
    student=Student.objects.get(pk=id)
    if request.method == 'POST':
        form=Student_Form(request.POST,instance=student)
        if form.is_valid():
            form.save()
            form=Student_Form()
        print(student,"--------------")
    else:
        form=Student_Form(instance=student)
    return render(request,'regform.html',{'form':form})





def success(request):
    return render(request,'success.html')
