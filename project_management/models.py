from django.db import models
from utility.models import BaseModel,UserProfile
from utility.models import PredfinedPointsRule,TaskUnitsPointsBaseModel
from hr.models import Employee,Employee_Achievement
# Create your models here.
class Project(TaskUnitsPointsBaseModel):
	name                      =  models.CharField(max_length=255, blank=True, null=True) 
	description               =  models.TextField(blank=True, null=True)
	location                  =  models.CharField(max_length=255, blank=True, null=True) 
	project_cost              =  models.DecimalField(default="0.00",max_digits=12,decimal_places=2) 
	estimated_cost            =  models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	actual_cost               =  models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	start_date                =  models.DateTimeField(blank=True, null=True) 
	end_date                  =  models.DateTimeField(blank=True, null=True) 	
	status                    = models.CharField(max_length=32, choices=(('pending','pending'),('completed','completed')), blank=True) 

class ProjectManager(models.Model):
	project                  = models.ForeignKey(Project, blank=True, null=True,related_name='ProjectManage',on_delete=models.CASCADE)
	project_manager          = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)
	start_date               = models.DateTimeField(blank=True, null=True)
	comments                 = models.TextField(blank=True, null=True)
	status                    = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True) 

class Task(BaseModel):
	project                  = models.ForeignKey(Project, blank=True, null=True,related_name='ProjectTask',on_delete=models.CASCADE)
	assigned_to              = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)
	description              = models.TextField(blank=True, null=True)
	total_units_task         = models.DecimalField(default="0.00",max_digits=12,decimal_places=2) 
	estimated_time_duration  = models.DecimalField(verbose_name="Estimated Time Duration in Hours",default="0.00",max_digits=12,decimal_places=2)
	start_date               = models.DateField(blank=True, null=True) 
	start_time               = models.TimeField( blank=True, null=True)
	end_date                 = models.DateField(blank=True, null=True) 
	end_time                 = models.TimeField( blank=True, null=True)

class TaskPerformed(models.Model):
	task                     = models.ForeignKey(Task, blank=True, null=True,on_delete=models.CASCADE)
	no_of_units_completed    = models.DecimalField(default="0.00",max_digits=12,decimal_places=2) 
	percent_completion       = models.DecimalField(default="0.00",max_digits=12,decimal_places=2) 
	total_task_time          = models.DecimalField(verbose_name="Total task time in Hours",default="0.00",max_digits=12,decimal_places=2)
	comments                 = models.TextField(blank=True, null=True)
	start_date               = models.DateField(blank=True, null=True) 
	start_time               = models.TimeField( blank=True, null=True)
	end_date                 = models.DateField(blank=True, null=True) 
	end_time                 = models.TimeField( blank=True, null=True)

class TaskPerformedReport(models.Model):
    taskperformed        = models.ForeignKey(TaskPerformed, blank=True, null=True,on_delete=models.CASCADE)
    project_manager      = models.ForeignKey(UserProfile, blank=True, null=True,on_delete=models.CASCADE)
    employee_achievement = models.ForeignKey(Employee_Achievement, blank=True, null=True,on_delete=models.CASCADE)
    comments             = models.TextField(blank=True, null=True)
    status               = models.CharField(max_length=32, choices=(('pending','pending'),('completed','completed')), blank=True) 


class OverTime(TaskUnitsPointsBaseModel):
	employee                   = models.ForeignKey(Employee, blank=True, null=True,related_name="OverTime",on_delete=models.CASCADE)
	overtime_manager           = models.ForeignKey(Employee, blank=True, null=True,related_name="OverTimeManager",on_delete=models.CASCADE)
	task                       = models.ForeignKey(Task, blank=True, null=True,on_delete=models.CASCADE)
	subject                    = models.CharField(max_length=255,blank=True, null=True)
	description                = models.TextField(blank=True, null=True)
	date_from                  = models.DateField( blank=True, null=True)
	time_from                  = models.TimeField( blank=True, null=True)
	date_to                    = models.DateField( blank=True, null=True)
	time_to                    = models.TimeField( blank=True, null=True)
	total_in_hrs               = models.CharField(max_length=255, blank=True, null=True)
	rate_per_hour              = models.DecimalField(default="0.00",max_digits=12,decimal_places=2) 
	total_cost                 = models.DecimalField(default="0.00",max_digits=12,decimal_places=2) 
	comments                   = models.TextField(blank=True, null=True)	
	status                     = models.CharField(max_length=32, choices=(('approve','approve'),('reject','reject')), blank=True) 



