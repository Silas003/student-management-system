from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm




def home(request):
    return render(request,'home.html',{})


def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New user created successfully!')
            return redirect('login')
        return render(request,'register.html',{'form':form}) 
    
    form=UserCreationForm()
    return render(request,'register.html',{'form':form}) 

def loginpage(request):
    # if request.method=="POST":
        
    #     user=request.POST['username']
    #     password=request.POST['password']
    #     user =authenticate(request,username=user,password=password)
    #     if user is not None:
    #         login(request,user)
    #         return redirect('home')
    #     else:
    #         message='Either Username or password incorrect!'
    #         return render(request,'login.html',{'message':message,'fail':True})
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request,'login.html', {})
    
    
def logoutpage(request):
    logout(request)
    return redirect('home')
        

