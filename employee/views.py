from django.shortcuts import render,redirect
from .models import EmployeeDeatail,User,EmployeeExperience,EmployeeEducation,EmployeeLoginLog
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone
from django.contrib.auth.decorators import login_required




def index (request):
    return render(request, 'index.html')

def registration(request):
    error = "" 

    if request.method == 'POST':
        fn = request.POST["firstname"]
        ln = request.POST["lastname"]
        ec = request.POST["empcode"]
        email = request.POST["email"]
        pwd = request.POST["pwd"]  
        try :  
         user = User.objects.create_user(first_name=fn, last_name=ln, username=email, password=pwd,)
         EmployeeDeatail.objects.create(user=user,empcode =ec)
         EmployeeExperience.objects.create(user=user, )
         EmployeeEducation.objects.create(user=user,)
         error = "no"
        except:
            error ="yes"
       

    return render(request, 'registration.html', {'error': error})


def emp_login(request):
    error = ""
    if request.method == "POST":
        u =request.POST['emailid']
        p =request.POST['password']
        user = authenticate(username = u, password = p)
        if user :
            login(request,user)
            error = "no"
        else :
            error  = "yes"  

    return render(request, 'emp_login.html',{'error': error})


@login_required
def emp_home(request):
    
    log = EmployeeLoginLog.objects.filter(employee=request.user, logout_time__isnull=True).first()
    
    if request.method == "POST":
        
        if not log: 
            EmployeeLoginLog.objects.create(employee=request.user, login_time=timezone.now())
        else:  
            log.logout_time = timezone.now()
            log.save()
        return redirect('emp_home')  
    
    context = {'is_logged_in': bool(log)}
    return render(request, 'emp_home.html', context)


def profile(request):
 
    error = "" 
    user=request.user
    employee= EmployeeDeatail.objects.get(user=user)

    if request.method == 'POST':
        fn = request.POST["firstname"]
        ln = request.POST["lastname"]
        ec = request.POST["empcode"]
        dept =request.POST["department"]
        designation = request.POST["designation"]
        ct = request.POST["contact"]  
        jdate = request.POST["jdate"] 
        gender = request.POST["gender"] 


        employee.user.first_name =fn
        employee.user.last_name =ln
        employee.empcode =ec
        employee.empdept =dept
        employee.designation =designation
        employee.contact =ct
        employee.gender =gender

        employee.joiningDate =jdate


        try :  
         employee.save()
         employee.user.save()
         error = "no"
         return redirect('profile')
        except:
            error ="yes"
       
    return render(request, 'profile.html', {'error': error, 'user': user, 'employee': employee})


def Logout (request):
     logout(request)
     return redirect('index')



def myexperience(request):
    error = "" 
    user = request.user
    try:
        experience = EmployeeExperience.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        experience = None  
    return render(request, 'myexperience.html', {'experience': experience, 'error': error})

def edit_experience(request):
    error = "" 
    user = request.user
    
   
    try:
        experience = EmployeeExperience.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        error = "Experience not found for this user"
        return render(request, 'edit_experience.html', {'error': error})

    if request.method == 'POST':
        
        company1name = request.POST.get("company1name", "")
        company1desig = request.POST.get("company1desig", "")
        company1salary = request.POST.get("company1salary", "")
        company1duration = request.POST.get("company1duration", "")

        company2name = request.POST.get("company2name", "")
        company2desig = request.POST.get("company2desig", "")
        company2salary = request.POST.get("company2salary", "")
        company2duration = request.POST.get("company2duration", "")

        company3name = request.POST.get("company3name", "")
        company3desig = request.POST.get("company3desig", "")
        company3salary = request.POST.get("company3salary", "")
        company3duration = request.POST.get("company3duration", "")

      
        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
           
            return redirect('myexperience')
        except Exception as e:
            error = "yes"
            

    return render(request, 'edit_experience.html', {'experience': experience, 'error': error})


def my_education(request):
    error = "" 
    user=request.user
    education= EmployeeEducation.objects.get(user=user)
    context ={
        'error ' : error ,
        'education' : education,

    }


    return render(request, 'my_education.html', context)

def edit_my_education(request):
    error = "" 
    user=request.user
    education= EmployeeEducation.objects.get(user=user)

    if request.method == 'POST':
        
        coursepg =request.POST["coursepg"]
        schoolclgpg =request.POST["schoolclgpg"]
        percentagepg =request.POST["percentagepg"]
       

        coursegra =request.POST["coursegra"]
        schoolclggra =request.POST["schoolclggra"]
        percentagera =request.POST["percentagera"]
        yearofpassingra =request.POST["yearofpassingra"]


        coursessc =request.POST["coursessc"]
        schoolclgssc =request.POST["schoolclgssc"]
        yearofpassingssc =request.POST["yearofpassingssc"]
        percentagessc =request.POST["percentagessc"]
   
      
        coursehsc =request.POST["coursehsc"]
        schoolclghsc =request.POST["schoolclgssc"]
        yearofpassinghsc =request.POST["yearofpassinghsc"]
        percentagehsc =request.POST["percentagehsc"]

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.percentagepg = percentagepg
        

        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.percentagera = percentagera
        education.yearofpassingra = yearofpassingra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc 

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc 

        try :
            education.save()
            education.user.save()
            error = "no"
            return redirect('my_education')
        
        
        except :
             error ="yes"

    return render(request, 'edit_my_education.html', locals())


def change_password(request):
    error = "" 
    user=request.user
    if request.method == 'POST':
        c= request.POST['currentpassword']
        n= request.POST['newpassword']
        try :
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"   
        
        
        except :
             error ="yes"

    return render(request, 'change_password.html', locals())


# admin



 

def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                error = "no" 
            else:
                error = "yes"
        else:
            error = "not" 

    return render(request, 'admin_login.html', {'error': error})


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    return render(request, 'admin_home.html')

def admin_profile(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    return render(request, 'admin_profile.html')



def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    employee = EmployeeDeatail.objects.all()
    print(employee)  

    return render(request, 'all_employee.html', locals())




def is_admin(user):
    return user.is_superuser



@user_passes_test(is_admin)
def admin_page(request):
    logs = EmployeeLoginLog.objects.all()
    return render(request, 'admin_page.html', {'logs': logs})


def admin_change_password (request):
    error = "" 
    user=request.user
    if request.method == 'POST':
        c= request.POST['currentpassword']
        n= request.POST['newpassword']
        try :
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"   
        
        
        except :
             error ="yes"

    return render(request, 'admin_change_password.html', locals())