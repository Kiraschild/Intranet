from emp_engagement.models import user_credentials, user_data

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .decorators import login_access_only, isUser

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
            user= user_data.objects.get(Username=username)
            print(user)
            print(user.is_user)
            if user.Password == password and user.is_user== True:
                request.session['username'] = username
                display_name= user.FirstName + " " + user.LastName
                quali= user.Qualifications
                profile_pic_url= user.Profilepic.url
                request.session['display_name']= display_name
                request.session['quali']=quali
                request.session['profile_pic_url']=profile_pic_url
                print(profile_pic_url)
                messages.success(request,"Successfully logged in!")
                print("User logged in",user)
                return render(request,'index.html',{'display_name': display_name, 'quali':quali, 'profile_pic_url':profile_pic_url})
            else :
                messages.error(request,"Check Credentials")
                return render(request,'login.html')

        except user_data.DoesNotExist:
            messages.error(request, "Invalid username")
            return redirect("/login")
            
    return render(request,'login.html')

def register_user(request): 
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        firstname=request.POST.get('fname')
        middlename=request.POST.get('mname')
        lastname=request.POST.get('lname')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        country=request.POST.get('country')
        dateofbirth=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        position=request.POST.get('position')
        department=request.POST.get('department')
        reportsto=request.POST.get('reportsto')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phno')
        profilepic = request.FILES.get('profilepic') 
        print(profilepic)
        if profilepic == None and gender=="M":
            profilepic="profile_pics/default_male_pic.png"
        elif profilepic == None and gender == "F":
            profilepic = "profile_pics/default_female_pic.png" 
        if password == "":
            password="admin123"
        print(username)
        print(password)
        print(firstname)
        print(middlename)
        print(lastname)
        print(profilepic)
        USERDATA = user_data.objects.create(
            Username=username,
            Password=password,
            FirstName= firstname,
            MiddleName= middlename,
            LastName= lastname,
            Address= address,
            City= city,
            State= state,
            Pincode= pincode,
            Country = country,
            DateofBirth= dateofbirth,
            Gender= gender,
            Qualifications= qualification,
            Position = position,
            Department = department,
            Reportsto = reportsto,
            Email= email,
            Phone_number= phonenumber,
            Profilepic = profilepic
            )
        print(user)
        USERDATA.save()
        return render(request,'login.html')
        
                 
    return render(request,'register.html')

@login_access_only
def logout_user(request):
    logout(request)
    messages.info(request, "Logged out Successfully!")
    return redirect('/login')

@login_access_only
def index(request): 
    #user= user_data.objects.get(Username=request.session.Username)
    display_name= request.session.get('display_name')
    quali = request.session.get('quali')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'index.html',{'display_name': display_name, 'quali':quali, 'profile_pic_url':profile_pic_url})

@login_access_only
def home(request): 
    display_name= request.session.get('display_name')
    quali = request.session.get('quali')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'home.html',{'display_name': display_name, 'quali':quali, 'profile_pic_url':profile_pic_url})

@login_access_only
def dashboard(request): 
    display_name= request.session.get('display_name')
    quali = request.session.get('quali')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'dashboard.html',{'display_name': display_name, 'quali':quali, 'profile_pic_url':profile_pic_url})
    

@login_access_only
def user(request): 
    display_name= request.session.get('display_name')
    quali = request.session.get('quali')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'user.html',{'display_name': display_name, 'quali':quali, 'profile_pic_url':profile_pic_url})

@login_access_only
def event(request): 
    display_name= request.session.get('display_name')
    quali = request.session.get('quali')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'event.html',{'display_name': display_name, 'quali':quali, 'profile_pic_url':profile_pic_url})

@login_access_only
def task(request): 
    display_name= request.session.get('display_name')
    quali = request.session.get('quali')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'task.html',{'display_name': display_name, 'quali':quali, 'profile_pic_url':profile_pic_url})

@login_access_only
def timesheet(request): 
    display_name= request.session.get('display_name')
    quali = request.session.get('quali')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'timesheet.html',{'display_name': display_name, 'quali':quali, 'profile_pic_url':profile_pic_url})

@login_access_only
def leave(request): 
    display_name= request.session.get('display_name')
    quali = request.session.get('quali')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'leave.html',{'display_name': display_name, 'quali':quali, 'profile_pic_url':profile_pic_url})