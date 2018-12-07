from django.shortcuts import render, redirect
from todo.models import Task
from todo.forms import TaskForm
from todo.models import Color


def home(request):
    tasks = Task.objects.all().order_by('is_done')
    return render(request, 'index.html', {'tasks': tasks})

def add(request):
    colors = Color.objects.all()
    form = TaskForm(request.POST or None)
    form_title = "Create Task"
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'task-form.html', {'form': form, 'colors': colors, 'form_title': form_title})

def update(request, id):
    colors = Color.objects.all()
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    form_title = "Edit Task"
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'task-form.html', {'form': form, 'task': task, 'colors': colors, 'form_title': form_title})

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')

def task_complete(request, id):
    is_done = not Task.objects.get(id=id).is_done
    Task.objects.filter(id=id).update(is_done=is_done)
    return redirect('/')

def search(request):
    query = request.GET.get('title')
    tasks = Task.objects.filter(title__contains=query)
    return render(request, 'index.html', {'tasks': tasks})




