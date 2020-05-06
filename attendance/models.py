from django.db import models
from utility.models import BaseModel,UserProfile
from hr.models import Employee
# Create your models here.


class Attendance(models.Model):
	employee           = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)
	enterance_date     = models.DateField( blank=True, null=True)
	enterance_time     = models.TimeField( blank=True, null=True)
	deperature_date    = models.DateField( blank=True, null=True)
	deperature_time    = models.TimeField( blank=True, null=True)
	entry_card_status  = models.CharField(max_length=32, choices=(('accept','accept'),('deny','deny')), blank=True) 
	comments           = models.TextField(blank=True, null=True)

class in_out_track(models.Model):
	atendance          = models.ForeignKey(Attendance, blank=True, null=True,on_delete=models.CASCADE)
	time_occure        = models.TimeField( blank=True, null=True)
	in_out             = models.CharField(max_length=32, choices=(('in','in'),('out','out')), blank=True) 
	entry_card_status  = models.CharField(max_length=32, choices=(('accept','accept'),('deny','deny')), blank=True) 
	comments           = models.TextField(blank=True, null=True)


class LeaveApplication(models.Model):
	employee           = models.ForeignKey(Employee, blank=True, null=True, related_name="LeaveApplicant",on_delete=models.CASCADE)
	hr_manager         = models.ForeignKey(Employee, blank=True, null=True,related_name="HRManagerProcess",on_delete=models.CASCADE)
	subject            = models.CharField(max_length=255,blank=True, null=True)
	description        = models.TextField(blank=True, null=True)
	date_from          = models.DateField( blank=True, null=True)
	time_from          = models.TimeField( blank=True, null=True)
	end_date           = models.DateField( blank=True, null=True)
	end_time           = models.TimeField( blank=True, null=True)
	total_in_hrs       = models.CharField(max_length=255, blank=True, null=True)
	comments           = models.TextField(blank=True, null=True)
	status             = models.CharField(max_length=32, choices=(('approve','approve'),('reject','reject')), blank=True) 

class LeaveApplicationDetails(models.Model):	
	leave_application    = models.ForeignKey(LeaveApplication, blank=True, null=True,related_name="LeaveApplicationDetails",on_delete=models.CASCADE)
	comment_by           = models.ForeignKey(Employee, blank=True, null=True,related_name="CommentBy",on_delete=models.CASCADE)
	comments             = models.TextField(blank=True, null=True)

class Leave(models.Model):
	leave_application   = models.ForeignKey(LeaveApplication, blank=True, null=True,related_name="LeaveApplication",on_delete=models.CASCADE)
	leave_type          = models.CharField(max_length=32, choices=(('Official','Official'),('Casual','Casual')), blank=True) 
	date_from           = models.DateField( blank=True, null=True)
	time_from           = models.TimeField( blank=True, null=True)
	end_date            = models.DateField( blank=True, null=True)
	end_time            = models.TimeField( blank=True, null=True)
	total_in_hrs        = models.CharField(max_length=255, blank=True, null=True)
	comments            = models.TextField(blank=True, null=True)
	status              = models.CharField(max_length=32, choices=(('approve','approve'),('rejected','rejected')), blank=True) 


