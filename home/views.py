from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages



def home(request):

    if request.method == 'POST':
        # Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        task = Task(taskTitle=title, taskDesc=desc)
        task.save()
        messages.success(request, "Task added successfully.")
        return redirect('/')

    return render(request, 'index.html')



def tasks(request):
    allTasks = Task.objects.all()
    
    if request.method == 'POST':
        task_id = request.POST.get('task-id')
        task = Task.objects.filter(id=task_id).first()
        if task is not None:
            task.delete()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

