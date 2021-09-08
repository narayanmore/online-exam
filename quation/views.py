from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def quations(request):
    s='quation is under proceses'
    return HttpResponse(s)
