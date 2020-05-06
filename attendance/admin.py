from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from attendance.models import  Attendance,in_out_track,LeaveApplication,LeaveApplicationDetails,Leave

class in_out_trackInline(admin.TabularInline):
    model = in_out_track
    extra = 1     

class AttendanceAdmin(admin.ModelAdmin):
    model = Attendance
    inlines = [in_out_trackInline]

class LeaveApplicationDetailsInline(admin.TabularInline):
    model = LeaveApplicationDetails
    extra = 1     

class LeaveApplicationAdmin(admin.ModelAdmin):
    model = LeaveApplication
    inlines = [LeaveApplicationDetailsInline]  

class LeaveAdmin(admin.ModelAdmin):
    model = Leave


admin.site.register(Attendance, AttendanceAdmin) 
admin.site.register(LeaveApplication, LeaveApplicationAdmin) 
admin.site.register(Leave, LeaveAdmin)      
