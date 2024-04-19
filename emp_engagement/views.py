from django.utils import timezone
import uuid
from emp_engagement.models import user_credentials, user_data, Event, TimeSheetData
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .decorators import login_access_only, isUser
import datetime

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
                display_name= user.FirstName + " " + user.LastName
                quali= user.Qualifications
                profile_pic_url= user.Profilepic.url
                request.session['username'] = username
                request.session['password'] = password
                request.session['firstname']= user.FirstName
                request.session['middlename']= user.MiddleName
                request.session['lastname']= user.LastName
                request.session['display_name']= display_name
                request.session['address1']= user.Address1
                request.session['address2']= user.Address2
                request.session['city']= user.City
                request.session['state']= user.State
                request.session['country']= user.Country
                request.session['pincode']= user.Pincode
                #request.session['dob']= user.DateofBirth
                if user.Gender == 'M':
                    request.session['gender']= "Male"
                elif user.Gender == 'F':
                    request.session['gender'] = "Female"
                else:
                    request.session['gender']= "Others"
                request.session['quali']=quali
                request.session['position']= user.Position
                request.session['department']= user.Department
                request.session['reports']= user.Reportsto
                request.session['email']= user.Email
                request.session['phone_number']= user.Phone_number
                request.session['profile_pic_url']=profile_pic_url
                print(profile_pic_url)
                messages.success(request,"Successfully logged in!")
                print("User logged in",user)
                return render(request,'index.html',{'display_name': display_name, 'position':user.Position, 'profile_pic_url':profile_pic_url})
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
        address1=request.POST.get('address1')
        address2= request.POST.get('address2')
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
            Address1= address1,
            Address2= address2,
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
    context = {
        'username': request.session.get('username'),
        'password': request.session.get('password'),
        'firstname': request.session.get('firstname'),
        'middlename': request.session.get('middlename'),
        'lastname': request.session.get('lastname'),
        'address1': request.session.get('address1'),
        'address2': request.session.get('address2'),
        'city': request.session.get('city'),
        'state': request.session.get('state'),
        'pincode': request.session.get('pincode'),
        'country': request.session.get('country'),
        #'dob': request.session.get('dob'),
        'gender': request.session.get('gender'),
        'quali': request.session.get('quali'),
        'position': request.session.get('position'),
        'department': request.session.get('department'),
        'reports': request.session.get('reports'),
        'email': request.session.get('email'),
        'phone_number': request.session.get('phone_number'),
        'profile_pic_url': request.session.get('profile_pic_url'),
        'display_name':request.session.get('display_name')
    }
    print(request.session.get('reports'))
    return render(request,'index.html',context)

@login_access_only
def home(request): 
    display_name= request.session.get('display_name')
    position = request.session.get('position')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'home.html',{'display_name': display_name, 'position':position, 'profile_pic_url':profile_pic_url})

@login_access_only
def dashboard(request): 
    display_name= request.session.get('display_name')
    position = request.session.get('position')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'dashboard.html',{'display_name': display_name, 'position':position, 'profile_pic_url':profile_pic_url})
    

@login_access_only
def user(request): 
    
    context = {
        'username': request.session.get('username'),
        'password': request.session.get('password'),
        'firstname': request.session.get('firstname'),
        'middlename': request.session.get('middlename'),
        'lastname': request.session.get('lastname'),
        'address1': request.session.get('address1'),
        'address2': request.session.get('address2'),
        'city': request.session.get('city'),
        'state': request.session.get('state'),
        'pincode': request.session.get('pincode'),
        'country': request.session.get('country'),
        #'dob': request.session.get('dob'),
        'gender': request.session.get('gender'),
        'quali': request.session.get('quali'),
        'position': request.session.get('position'),
        'department': request.session.get('department'),
        'reports': request.session.get('reports'),
        'email': request.session.get('email'),
        'phone_number': request.session.get('phone_number'),
        'profile_pic_url': request.session.get('profile_pic_url'),
        'display_name':request.session.get('display_name')
    }
    if request.method =="POST":
        if 'passwordChange' in request.POST:
            currentUser = request.session.get('username')
            password = request.session.get('password')
            currentPassword = request.POST.get("currentPassword")
            newPassword= request.POST.get("newPassword")
            confirmPassword = request.POST.get("confirmPassword")
            if password == currentPassword:
                if newPassword != currentPassword:
                    if newPassword == confirmPassword:
                        print("Successfull")
                        user= user_data.objects.get(Username=currentUser)
                        user.Password = newPassword
                        user.save()
                        #user.user_data.save()
                        request.session['password'] = newPassword
                        context = {
                        'username': request.session.get('username'),
                        'password': request.session.get('password'),
                        'firstname': request.session.get('firstname'),
                        'middlename': request.session.get('middlename'),
                        'lastname': request.session.get('lastname'),
                        'address1': request.session.get('address1'),
                        'address2': request.session.get('address2'),
                        'city': request.session.get('city'),
                        'state': request.session.get('state'),
                        'pincode': request.session.get('pincode'),
                        'country': request.session.get('country'),
                        #'dob': request.session.get('dob'),
                        'gender': request.session.get('gender'),
                        'quali': request.session.get('quali'),
                        'position': request.session.get('position'),
                        'department': request.session.get('department'),
                        'reports': request.session.get('reports'),
                        'email': request.session.get('email'),
                        'phone_number': request.session.get('phone_number'),
                        'profile_pic_url': request.session.get('profile_pic_url'),
                        'display_name':request.session.get('display_name')
                        }
                        return render(request, 'user.html', context)    
                    else:
                        print("passwords dont match")
                else:
                    print("password is same as previous password")
            else:
                print("current password does not match")    
        
        if 'addressChange' in request.POST:
            currentUser = request.session.get('username')
            newAddress1 = request.POST.get('new_address_line_1')
            newAddress2 = request.POST.get('new_address_line_2')
            newCity = request.POST.get('new_city')
            newPincode = request.POST.get('new_pincode')
            newState = request.POST.get('new_state')
            newCountry = request.POST.get('new_country')
            user= user_data.objects.get(Username=currentUser)
            user.Address1 = newAddress1
            user.Address2 = newAddress2
            user.City= newCity
            user.Pincode= newPincode
            user.State= newState
            user.Country= newCountry
            user.save()
            request.session['address1']= newAddress1
            request.session['address2']= newAddress2
            request.session['city']= newCity
            request.session['pincode']= newPincode
            request.session['state']= newState
            request.session['country']= newCountry
            context = {
            'username': request.session.get('username'),
            'password': request.session.get('password'),
            'firstname': request.session.get('firstname'),
            'middlename': request.session.get('middlename'),
            'lastname': request.session.get('lastname'),
            'address1': request.session.get('address1'),
            'address2': request.session.get('address2'),
            'city': request.session.get('city'),
            'state': request.session.get('state'),
            'pincode': request.session.get('pincode'),
            'country': request.session.get('country'),
            #'dob': request.session.get('dob'),
            'gender': request.session.get('gender'),
            'quali': request.session.get('quali'),
            'position': request.session.get('position'),
            'department': request.session.get('department'),
            'reports': request.session.get('reports'),
            'email': request.session.get('email'),
            'phone_number': request.session.get('phone_number'),
            'profile_pic_url': request.session.get('profile_pic_url'),
            'display_name':request.session.get('display_name')
            }
            return render(request,'user.html',context)
    return render(request,'user.html',context)

@login_access_only
def event(request): 
    currentUser = request.session.get('username')
    display_name= request.session.get('display_name')
    position = request.session.get('position')
    profile_pic_url = request.session.get('profile_pic_url')

    if request.method == 'POST':
        current_user = currentUser
        event_id = str(uuid.uuid4())[:6]
        title = request.POST.get('event-title')
        start = request.POST.get('event-start')
        end = request.POST.get('event-end')
        details = request.POST.get('event-details')


        # Create the event associated with the logged-in user
        event = Event.objects.create(
            eventid=event_id,
            username=current_user,
            title=title,
            start=start,
            end=end,
            details=details
        )
        event.save()

        return redirect('event')

    else:
        # events = Event.objects.filter(username=currentUser)
        events = Event.objects.all()
        event_data = Event.objects.filter(username=request.session.get('username'))
        return render(request,'event.html',{'display_name': display_name, 'position':position, 'profile_pic_url':profile_pic_url, 'events': event_data})


@login_access_only
def task(request): 
    display_name= request.session.get('display_name')
    position = request.session.get('position')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'task.html',{'display_name': display_name, 'position':position, 'profile_pic_url':profile_pic_url})

@login_access_only
def timesheet(request):
    timezone.activate("Asia/Kolkata")
    display_name= request.session.get('display_name')
    position = request.session.get('position')
    profile_pic_url = request.session.get('profile_pic_url') 
    if request.method == 'POST':
        username = request.session.get('username')  # Retrieve username from session
        if 'check_in' in request.POST:
            # Handle login action
            TimeSheetData.objects.create(username=username, check_in_time=timezone.localtime(timezone.now()))
        elif 'check_out' in request.POST:
            # Handle logout action
            last_entry = TimeSheetData.objects.filter(username=username).order_by('-date', '-check_in_time').first()

            print(last_entry.check_in_time)
            if last_entry:
                last_entry.check_out_time = timezone.localtime(timezone.now()).time()
                # temp_last_check_in_time = last_entry.check_in_time
                # print("Check in:",temp_last_check_in_time)
                # print("Check out",last_entry.check_out_time)

                t1 = last_entry.check_in_time
                t2 = last_entry.check_out_time

                t1_seconds = t1.hour * 3600 + t1.minute * 60 + t1.second
                t2_seconds = t2.hour * 3600 + t2.minute * 60 + t2.second

                difference_seconds = t2_seconds - t1_seconds

                hours = difference_seconds // 3600
                minutes = (difference_seconds % 3600) // 60
                seconds = difference_seconds % 60


                # last_entry.total_time = datetime.time(hour=hours, minute=minutes, second=seconds)
                time_diff = datetime.time(hour=hours, minute=minutes, second=seconds)

                last_entry.total_time = time_diff.strftime("%H:%M:%S")

                # last_entry.total_time = last_entry.check_out_time - last_entry.check_in_time
                print(last_entry.total_time)
                last_entry.save()

            # if last_entry:
            #     last_entry.check_out_time = timezone.localtime(timezone.now())
            #     last_entry.total_time = last_entry.check_out_time - last_entry.check_in_time
            #     last_entry.save()


        return redirect('timesheet')

    timesheet_data = TimeSheetData.objects.filter(username=request.session.get('username'))
      
    return render(request,'timesheet.html',{'display_name': display_name, 'position':position, 'profile_pic_url':profile_pic_url,'timesheet_data': timesheet_data})

@login_access_only
def leave(request): 
    display_name= request.session.get('display_name')
    position = request.session.get('position')
    profile_pic_url = request.session.get('profile_pic_url')
    return render(request,'leave.html',{'display_name': display_name, 'position':position, 'profile_pic_url':profile_pic_url})