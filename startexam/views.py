from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def startexam(request):
    #if request.session.has_key('username'):
    #if 'username' in request.session:
    if 'username' not in request.session:
        s='http://localhost:8000/login/login/'
        return HttpResponseRedirect(s) 

    res=render(request,'startexam/startexam.html')
    return res
def fun_logout(request):
    logout(request)
    s='http://localhost:8000/login/login/'
    return HttpResponseRedirect(s)    
