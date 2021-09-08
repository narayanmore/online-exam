from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def registration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username all ready taken')
                s='http://localhost:8000/login/regi/'
                return HttpResponseRedirect(s)
               
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email all ready teaken')
                s='http://localhost:8000/login/regi/'
                return HttpResponseRedirect(s)
              
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('user created')
                s='http://localhost:8000/login/login'
                return HttpResponseRedirect(s)
        else:
            messages.info(request,'password1 and  password 2 is not maching')
            s='http://localhost:8000/login/regi/'
            return HttpResponseRedirect(s)

    else:
        res=render(request,'login/regi.html')
        return res

def loginfun(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            print("welcome")
            s='http://localhost:8000/startexam/startexam/'
            return HttpResponseRedirect(s)
        else:
            print('enter correct username and password')
            s='http://localhost:8000/login/login'
            return HttpResponseRedirect(s)    
    else: 

         res=render(request,'login/login.html')
         return res
  