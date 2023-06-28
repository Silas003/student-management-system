from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import StudentForm,UserForm


def home(request):
    
    student=Student.objects.all()
    return render(request,'home.html',{'student':student})

def add(request):
    if request.method =="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            newID=form.cleaned_data['StudentID']
            newName=form.cleaned_data['StudentName']
            newEmail=form.cleaned_data['Email']
            newCollege=form.cleaned_data['College']
            newPOS=form.cleaned_data['POS']
            newYOA=form.cleaned_data['YOA']
            new_student=Student(StudentID=newID,
                                StudentName=newName,
                                Email=newEmail,
                                College=newCollege,
                                POS=newPOS,
                                YOA=newYOA)
            new_student.save()
            message=messages.success(request,'student add successfully!')
            
            return render(request,'add.html',{'form':form,'message':message,'success':True})
    else:
        form=StudentForm()
        return render(request,'add.html',{'form':form})
    
def view(request,id):
    student=Student.objects.get(pk=id)
    
    return render(request,'view.html',{'student':student,})
def update(request,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return render(request,'update.html',{'form':form,'student':student,'new':True})
    else:
        student=Student.objects.get(pk=id)
        form=StudentForm(instance=student)
        return render(request,'update.html',{'form':form,'student':student})
def delete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect('home')

def login(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            newN=form.cleaned_data['username']
            newE=form.cleaned_data['email']
            newp=form.cleaned_data['password']
            user=User(username=newN,email=newE,password=newp)
            user.save()
        return render(request,'login.html',{'success':True,'user':user})
    
    form=UserForm()
    return render(request,'login.html',{'form':form})

def logout(request):
    return redirect('home')