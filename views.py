from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, TaskForm
from .models import Task
from django.forms import ModelForm, TextInput, Textarea
def home(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница сайта', 'tasks': tasks})
    
def about(request):
    return render(request, 'about.html')

def lib(request):
    return render(request, 'lib.html') 

def signup(request):
    return render(request, 'registration/register.html') 

def login(request):
    return render(request, 'login.html') 

    
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

def log_out(request):
    return render(request, 'registration/log_out.html') 

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)