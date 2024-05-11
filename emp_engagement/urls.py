from django.contrib import admin
from django.urls import path
from emp_engagement import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('login', views.login_user, name='login_user'),
    path('register',views.register_user, name="register"),
    path("logout",views.logout_user,name="logout_user"),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user', views.user, name='user'),
    path('adminuser',views.adminuser, name='Admin User'),
    path('delete_user/<str:username>', views.delete_user, name='delete_user'),
    path('event', views.event, name='event'),
    path('task', views.task, name='task'),
    path('timesheet', views.timesheet, name='timesheet'),
    path('leave', views.leave, name='leave'),
    path('manageadmin',views.manageadmin, name='Admin Page'),
    path('activeusers',views.activeusers,name='Active Users'),
    path('policy',views.companypolicy, name='COmpany Policy'),
    path('checkinout',views.checkinout,name='Check-in Check-out'),
    path('holidayspage',views.holidays,name='Holiday List'),
    path('birthdays',views.birthday,name='Birthdays')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


AdminMenulist=[
    ['Home','/home','home'],
    ['Dashboard','/dashboard','grid-alt'],
    ['User','/user','user'],
    ['Event Calendar','/event','calendar'],
    ['Leave','/leave','envelope'],
    ['Tasks','/task','task'],
    ['Check-In Check-Out','/checkinout','check-circle'],
    ['Birthdays','/birthdays','cake'],
    ['Timesheet','/timesheet','time'],
    ['Holiday List','/holidayspage','landscape'],
    ['Company Policy','/policy','buildings'],
    ['Active Users','/activeusers','user-check'],
    ['Admin Page','/manageadmin','cog'],
    ['User Management','/user','group'],
    # ['Index','/index']
    
]

UserMenulist=[
    ['Home','/home','home'],
    ['Dashboard','/dashboard','grid-alt'],
    ['User','/user','user'],
    ['Event Calendar','/event','calendar'],
    ['Leave','/leave','envelope'],
    ['Tasks','/task','task'],
    ['Check-In Check-Out','/checkinout','check-circle'],
    ['Birthdays','/birthdays','cake'],
    ['Timesheet','/timesheet','time'],
    ['Holiday List','/holidayspage','landscape'],
    ['Company Policy','/policy','buildings'],
    # ['Index','/index']
]