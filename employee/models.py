from django.db import models
from django.contrib.auth.models import User


class EmployeeDeatail(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    empcode=models.CharField(max_length=50,null=True)
    empdept=models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=50,null=True)
    contact=models.CharField(max_length=50, null=True)
    gender=models.CharField(max_length=50,null=True)
    joiningDate = models.DateField(null=True)

    def __str__(self):
        return self.user.username
    
class EmployeeEducation(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)

    coursepg=models.CharField(max_length=100,null=True)
    schoolclgpg=models.CharField(max_length=200,null=True)
    percentagepg=models.CharField(max_length=50,null=True)

    coursegra=models.CharField(max_length=100, null=True)
    schoolclggra=models.CharField(max_length=200,null=True)
    yearofpassingra=models.CharField(max_length=50,null=True)
    percentagera=models.CharField(max_length=50,null=True)

    coursessc=models.CharField(max_length=100, null=True)
    schoolclgssc=models.CharField(max_length=200,null=True)
    yearofpassingssc=models.CharField(max_length=50,null=True)
    percentagessc=models.CharField(max_length=50,null=True)

    coursehsc=models.CharField(max_length=100, null=True)
    schoolclghsc=models.CharField(max_length=200,null=True)
    yearofpassinghsc=models.CharField(max_length=50,null=True)
    percentagehsc=models.CharField(max_length=30,null=True)
    

    def __str__(self):
        return self.user.username



        
class EmployeeExperience(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    company1name=models.CharField(max_length=100,null=True)
    comapny1desig=models.CharField(max_length=200,null=True)
    company1salary=models.CharField(max_length=100,null=True)
    comapny1duration=models.CharField(max_length=100, null=True)
    company2name=models.CharField(max_length=100,null=True)
    comapny2desig=models.CharField(max_length=200,null=True)
    company2salary=models.CharField(max_length=100,null=True)
    comapny2duration=models.CharField(max_length=100, null=True)
    company3name=models.CharField(max_length=100,null=True)
    comapny3desig=models.CharField(max_length=200,null=True)
    company3salary=models.CharField(max_length=100,null=True)
    comapny3duration=models.CharField(max_length=100, null=True)
  

    def __str__(self):
        return self.user.username    
   

    from django.db import models
from django.contrib.auth.models import User

class EmployeeLoginLog(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    
    def total_time(self):
        if self.logout_time:
            return self.logout_time - self.login_time
        return None 