from django.db import models  
class Employee(models.Model):  
        eid = models.CharField(max_length=20)
        ename = models.CharField(max_length=100) 
        ename = models.CharField(max_length=100)
        eage = models
        edate_of_birth = models.DateField()
        edate_of_employment = models.DateField()
        eposition = models.CharField(max_length=28)
        edepartment = models.CharField(max_length=28)
        esalary = models.CharField(max_length=8)
        esupervisors = models.CharField(max_length=28)
        class Meta:  
            db_table = "employee"  















