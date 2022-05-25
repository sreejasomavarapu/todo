from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Taskform
from .models import *
# Create your views here.
def list(request):
    '''form=Taskform()
    content={'form':form}'''
    tasks=Task.objects.all()
    if request.method=="POST":
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form=Taskform()

    
    content={'tasks':tasks,'form':form}
    return render(request,'tasks/list.html',content)

def Update_task(request,pk):
    task_selected=Task.objects.get(id=pk)
    form=Taskform(instance=task_selected)
    content={'form':form}
    if request.method=="POST":
        form=Taskform(request.POST,instance=task_selected)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request,'tasks/update.html',content)

def Delete(request,pk):
    item=Task.objects.get(id=pk)
    form=Taskform(instance=item)
    context={'item':item,'form':form}

    if request.method=="POST":
        form=Taskform(request.POST,instance=item)
        item.delete()
        return redirect("/")

    

    return render(request,'tasks/delete.html',context)


