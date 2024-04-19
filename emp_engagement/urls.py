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
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
