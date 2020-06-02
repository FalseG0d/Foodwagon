from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import *

from .forms import *
#from django.contrib.auth.forms import UserCreationForm 
# Create your views here.

def logoutUser(request):
    logout(request)
    return redirect('/')

def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'home/register.html',{'form':form})


def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            return HttpResponse('Username or Password Incorrect')

    return render(request,'home/login.html')

@login_required(login_url='login')
def make_request(request):
    form=RequestForm()

    if request.method=='POST':

        form=RequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form,
    }

    return render(request,'home/request.html',context)

def home(request):

    #register=UserCreationForm()
    
    services=Service.objects.all()
    types=Type.objects.all()
    reviews=Review.objects.all()
    count=Request.objects.count()
    helpers=Helper.objects.all()
    helps=Help.objects.all()

    context={
        'services':services,
        'types':types,
        'reviews':reviews,
        'count':count,
        'helpers':helpers,
        'helps':helps,
    }

    return render(request,'home/dashboard.html',context)

#def User(request,pk):