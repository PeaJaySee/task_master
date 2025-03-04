from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    tasks_due = Task.objects.filter(complete=False)
    tasks_completed = Task.objects.filter(complete=True)
    return render(request, 'tasks/index.html', {'tasks_due': tasks_due, 'tasks_completed': tasks_completed, 'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')

context = {"complete_task": complete_task, "delete_task": delete_task}