from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task, TaskForm
from datetime import date
# Create your views here.

@login_required(login_url='/todolist/login')
def show_todolist(request):
    tasks = Task.objects.all()

    context = {
        'task_list': tasks,
        'user_name': request.COOKIES['user_name']
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login')
def add_new_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = get_user_model().objects.get(username=request.COOKIES['user_name'])
            task.date = date.today()
            task.save()
            return HttpResponseRedirect(request.path_info)
    context = {'form':form}
    return render(request, 'addtask.html', context)  


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Account sucessfully created!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('user_name', username)
            return response
        else :
            messages.info(request, 'Wrong Username or Password')
    context={}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response