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
    path('index/', views.index, name='index'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user', views.user, name='user'),
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
    ['User Task','/task'],
    ['Active Users','/activeusers'],
    ['Admin Page','/manageadmin'],
    ['User Management','/user'],
    ['Event Calendar','/event'],
    ['Check-In Check-Out','/checkinout'],
    ['Company Policy','/policy'],
    ['Leave Details','/leave'],
    ['Holiday List','/holidayspage'],
    ['Birthdays','/birthdays'],
    ['Timesheet','/timesheet'],
    ['Dashboard','/dashboard'],
    ['Home','/home'],
    ['Index','/index']
    
]

UserMenulist=[
    ['User Task','/task'],
    ['Event Calendar','/event'],
    ['Check-In Check-Out','/checkinout'],
    ['Company Policy','/policy'],
    ['Leave Details','/leave'],
    ['Holiday List','/holidayspage'],
    ['Birthdays','/birthdays'],
    ['Timesheet','/timesheet'],
    ['Dashboard','/dashboard'],
    ['Home','/home'],
    ['Index','/index']
]