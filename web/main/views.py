from django.shortcuts import render, redirect
from .forms import TaskForm, NewUserForm, ClassesForm
from .models import Task, Classes
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
def home(request):
    titles = Classes.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница сайта', 'titles': titles})
    
def about(request):
    return render(request, 'about.html')

def lib(request):
    return render(request, 'lib.html') 

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="account/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="account/login.html", context={"login_form":form}) 

def log_out(request):
	logout(request)
	return render(request, 'account/login.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = TaskForm()
    return render(request, 'create.html', {'form': form})

def themes(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'themes.html', {'title': 'Takiriptar', 'tasks': tasks})


def tasks(request):
    return render(request, 'tasks.html')

def videoles(request):
    return render(request, 'videoles.html')

def clas(request):
    error = ''
    if request.method == 'POST':
        form = ClassesForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = ClassesForm()
    return render(request, 'create.html', {'form': form})