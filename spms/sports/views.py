from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from .models import *
from .forms import CreateUserForm

def home(request):
    return render(request,'sports/index.html')
def about(request):
    return render(request,'sports/about.html')

def loginPage(request):
<<<<<<< HEAD
=======
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
>>>>>>> authentication
    return render(request,'sports/login.html')

def forgotpass(request):
    return render(request,'sports/forgotpass.html')

def registerAccount(request):
    form=CreateUserForm(request.POST)

    if request.method== 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
<<<<<<< HEAD
            messages.success(request,'account was created for '+ user)
            return redirect('login')
=======
            messages.success(request,'account was created for'+ user)
            return redirect('loginPage')
>>>>>>> authentication
    context={'form':form}
    return render(request,'sports/registerAccount.html',context)




