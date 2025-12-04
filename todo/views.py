from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    # return redirect('/home')
    return render(request,'index.html')