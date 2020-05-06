from django import forms
from attendance.models import *

from django.contrib.auth.models import User



class AttendanceFrom(forms.ModelForm):
	employee           = forms.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)
	enterance_date     = forms.DateField( blank=True, null=True)
	enterance_time     = forms.TimeField( blank=True, null=True)
	deperature_date    = forms.DateField( blank=True, null=True)
	deperature_time    = forms.TimeField( blank=True, null=True)
	entry_card_status  = forms.CharField(max_length=32, choices=(('accept','accept'),('deny','deny')), blank=True) 
	comments           = forms.TextField(blank=True, null=True)
	class Meta:
        model = Attendance
        fields = ('employee','enterance_date','enterance_time','deperature_date','deperature_time','entry_card_status')

class in_out_trackFrom(forms.ModelForm):
	atendance          = forms.ForeignKey(Attendance, blank=True, null=True,on_delete=models.CASCADE)
	time_occure        = forms.TimeField( blank=True, null=True)
	in_out             = forms.CharField(max_length=32, choices=(('in','in'),('out','out')), blank=True) 
	entry_card_status  = forms.CharField(max_length=32, choices=(('accept','accept'),('deny','deny')), blank=True) 
	comments           = forms.TextField(blank=True, null=True)
    class Meta:
        model = in_out_track
        fields = ('atendance','time_occure','in_out','entry_card_status','comments')

class LeaveApplicationFrom(forms.ModelForm):
	employee           = forms.ForeignKey(Employee, blank=True, null=True, related_name="LeaveApplicant",on_delete=models.CASCADE)
	hr_manager         = forms.ForeignKey(Employee, blank=True, null=True,related_name="HRManagerProcess",on_delete=models.CASCADE)
	subject            = models.CharField(max_length=255,blank=True, null=True)
	description        = forms.TextField(blank=True, null=True)
	date_from          = forms.DateField( blank=True, null=True)
	time_from          = forms.TimeField( blank=True, null=True)
	end_date           = forms.DateField( blank=True, null=True)
	end_time           = forms.TimeField( blank=True, null=True)
	total_in_hrs       = forms.CharField(max_length=255, blank=True, null=True)
	comments           = forms.TextField(blank=True, null=True)
	status             = forms.CharField(max_length=32, choices=(('approve','approve'),('reject','reject')), blank=True) 
    class Meta:
        model = LeaveApplication
        fields = ('employee','hr_manager','subject','description','date_from','time_from','end_date','end_time','total_in_hrs','comments','status')



class LeaveApplicationDetailsFrom(forms.ModelForm):	
	leave_application    = forms.ForeignKey(LeaveApplication, blank=True, null=True,related_name="LeaveApplicationDetails",on_delete=models.CASCADE)
	comment_by           = forms.ForeignKey(Employee, blank=True, null=True,related_name="CommentBy",on_delete=models.CASCADE)
	comments             = forms.TextField(blank=True, null=True)
	class Meta:
        model = LeaveApplicationDetails
        fields = ('leave_application','comment_by','comments')

class LeaveFrom(models.Model):
	leave_application   = forms.ForeignKey(LeaveApplication, blank=True, null=True,related_name="LeaveApplication",on_delete=models.CASCADE)
	leave_type          = forms.CharField(max_length=32, choices=(('Official','Official'),('Casual','Casual')), blank=True) 
	date_from           = forms.DateField( blank=True, null=True)
	time_from           = forms.TimeField( blank=True, null=True)
	end_date            = forms.DateField( blank=True, null=True)
	end_time            = forms.TimeField( blank=True, null=True)
	total_in_hrs        = forms.CharField(max_length=255, blank=True, null=True)
	comments            = forms.TextField(blank=True, null=True)
	status              = forms.CharField(max_length=32, choices=(('approve','approve'),('rejected','rejected')), blank=True) 
    class Meta:
        model = Leave
        fields = ('leave_application','leave_type','date_from','time_from','end_date','end_time','total_in_hrs','comments','status')

