from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
def home(request):
    # return redirect('/home')
    todo_list=Todo.objects.values_list('task', flat=True)
    context={'todo_list':todo_list}
    print(context)
    return render(request,'index.html',context)

def add_task(request):
    if request.method=='POST':
        task_input=request.POST.get('task-input')
        print("recieved input:",task_input)
        obj=Todo(
        task=task_input
        )
    obj.save()
    return redirect('/')