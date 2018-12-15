from django.shortcuts import render, redirect
from todo.models import Task
from todo.forms import TaskForm
from todo.models import Color
from todo.models import User


def home(request):
    user_id = request.session['user_id']
    tasks = Task.objects.filter(user_id=user_id).order_by('is_done')
    return render(request, 'index.html', {'tasks': tasks})

def add(request):
    colors = Color.objects.all()
    form = TaskForm(request.POST or None)
    form_title = "Create Task"
    user_id = request.session['user_id']
    if form.is_valid():
        form.save()
        return redirect('/tasks')
    return render(request, 'task-form.html', {'form': form,
                                              'colors': colors,
                                              'form_title': form_title,
                                              'user_id': user_id})

def update(request, id):
    colors = Color.objects.all()
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    form_title = "Edit Task"
    user_id = request.session['user_id']
    if form.is_valid():
        form.save()
        return redirect('/tasks')
    return render(request, 'task-form.html', {'form': form,
                                              'task': task,
                                              'colors': colors,
                                              'form_title': form_title,
                                              'user_id': user_id})

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/tasks')

def task_complete(request, id):
    is_done = not Task.objects.get(id=id).is_done
    Task.objects.filter(id=id).update(is_done=is_done)
    return redirect('/tasks')

def search(request):
    query = request.GET.get('title')
    user_id = request.session['user_id']
    tasks = Task.objects.filter(title__contains=query, user_id=user_id)
    return render(request, 'index.html', {'tasks': tasks})

def login(request):
    return render(request, 'login.html')

def sign_in(request):
    login = request.GET.get('login')
    password = request.GET.get('password')
    if User.objects.filter(login=login).exists():
        user = User.objects.get(login=login)
        if user.password == password:
            request.session['user_id'] = user.id
            return redirect('/tasks')
    return redirect('/')

def sign_out(request):
    return redirect('/')




