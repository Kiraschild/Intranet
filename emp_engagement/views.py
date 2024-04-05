from emp_engagement.models import user_credentials

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .decorators import login_access_only

# Create your views here.

def login_page(request):
    return render(request, 'login.html')

def login_user(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print("Username: ",username)
        print("Password: ",password)
        try:
            user= user_credentials.objects.get(username=username)
            print(user)
            if user.password == password:
                request.session['username'] = username
                messages.success(request,"Successfully logged in!")
                print("User logged in",user)
                return redirect('index/')
            else :
                messages.error(request,"Check Credentials")
                return render(request,'login.html')

        except user_credentials.DoesNotExist:
            messages.error(request, "Invalid username")
            return redirect("/login")
            
    return render(request,'login.html')

def register_user(request):
    return render(request,'register.html')

@login_access_only
def logout_user(request):
    logout(request)
    messages.info(request, "Logged out Successfully!")
    return redirect('/login')

@login_access_only
def index(request): 
    return render(request,'index.html')

@login_access_only
def home(request): 
    return render(request, 'home.html')

@login_access_only
def dashboard(request): 
    return render(request, 'dashboard.html')

@login_access_only
def user(request): 
    return render(request, 'user.html')

@login_access_only
def event(request): 
    return render(request, 'event_calendar.html')

@login_access_only
def task(request): 
    return render(request, 'task.html')

@login_access_only
def timesheet(request): 
    return render(request, 'timesheet.html')

@login_access_only
def leave(request): 
    return render(request, 'leave.html')