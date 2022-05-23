from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .decorators import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
def home(request):
    titles = Classes.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница сайта', 'titles': titles})
    
def about(request):
    return render(request, 'about.html')

def lib(request):
    books = Books.objects.order_by('-id')
    return render(request, 'lib.html', {'books': books}) 

@unauthenticated_user
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name = 'users')
			user.groups.add(group)
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
            
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
    
	return render (request=request, template_name="account/register.html", context={"register_form":form})
        

@unauthenticated_user
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
	return redirect('home') 


@allowed_users(allowed_roles=["admin"])
def create(request):
    error = ''
    if request.method == 'POST':
        form = ThemeForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = ThemeForm()
    return render(request, 'create.html', {'form': form})

def themes(request, classes):
    themes = Theme.objects.filter(classes=classes)
    return render(request, 'themes.html', {'title': 'Takiriptar', 'themes': themes, 'classes': classes})


def tasks(request, classes):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.filter(classes=classes)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'classes': classes
        }
        return render(request,'result.html',context)
    else:
        questions=QuesModel.objects.filter(classes=classes)
        context = {
            'questions':questions,
            'classes': classes
        }
        return render(request,'tasks.html',context, )

def videoles(request, classes):
    vid=Video.objects.filter(classes=classes)
    context = {
            'vid':vid,
            'classes': classes
        }
    return render(request, 'videoles.html', context)

@allowed_users(allowed_roles=["admin"])
def clas(request):
    error = ''
    if request.method == 'POST':
        form = ClassesForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = ClassesForm()
    return render(request, 'clas.html', {'form': form})

@allowed_users(allowed_roles=["admin"])
def addtask(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addtask.html',context)
    else: 
        return redirect('home')

@allowed_users(allowed_roles=["admin"])
def addvideo(request):    
    if request.method == 'POST':
        form = VideoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = VideoForm()
    return render(request, 'addvideo.html', {'form': form})

def addbook(request):
    error = ''
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = BooksForm()
    return render(request, 'addbook.html', {'form': form})