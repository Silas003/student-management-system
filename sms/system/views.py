from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import StudentForm,UserForm,Login
from django.contrib.auth import authenticate,login,logout


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

def register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'user created successfully')
            return render(request,'register.html',{'form':form})
    
    form=UserForm()
    return render(request,'register.html',{'form':form})

def loginpage(request):
    if request.method=="POST":
        form=Login(request.POST)
        
        user=form.cleaned_data['username']
        pass1=form.cleaned_data['password']
        user=authenticate(username=user,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,'user login successful')
            return redirect('home')
    form=Login()
    return render(request,'login.html',{'form':form})

def logoutpage(request):
    logout(request)
    return redirect('home')