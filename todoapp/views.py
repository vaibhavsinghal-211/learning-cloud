from django.shortcuts import render, redirect, get_object_or_404
from todoapp.models import Task
from .forms import TaskForm
# Create your views here.

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_tasks')
    return render(request, 'todoapp/task_form.html', {'form': form})

# Update task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'todoapp/task_form.html', {'form': form})

# Delete task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todoapp/task_confirm_delete.html', {'task': task})