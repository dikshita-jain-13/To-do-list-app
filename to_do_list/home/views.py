from multiprocessing import context
from django.shortcuts import render,HttpResponse
from home.models import Task

# Create your views here.

def home(request):
    context={'success':False,'name':'Dikshita'}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(tasktitle=title,taskdesc=desc)
        ins.save()
        context={'success':True}
    #return HttpResponse('works')
    
    return render(request,'index.html', context)

def tasks(request):
    #return HttpResponse('works')
    allTasks= Task.objects.all()
    print(allTasks)
    context={'tasks':allTasks}
    return render(request,'tasks.html',context)