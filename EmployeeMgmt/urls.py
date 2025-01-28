"""
URL configuration for EmployeeMgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('admin_profile/', views.admin_profile, name="admin_profile"),
    path('admin_change_password/',views.admin_change_password, name="admin_change_password"), 
    path('',views.index, name="index"),
    path('registration/',views.registration , name='registration'),
    path('emp_login/',views.emp_login, name="emp_login"),
    path('emp_home/',views.emp_home, name="emp_home"),
    path('profile/',views.profile, name="profile"),
    path('logout/',views.Logout, name="logout"),
    path('myexperience/',views.myexperience, name="myexperience"),
    path('edit_experience/',views.edit_experience, name="edit_experience"),
    path('my_education/',views.my_education, name="my_education"),
    path('edit_my_education/',views.edit_my_education, name="edit_my_education"), 
    path('change_password/',views.change_password, name="change_password"),
    path('all_employee/',views.all_employee, name="all_employee"),
    path('admin_page/', views.admin_page, name='admin_page'),
    


]

