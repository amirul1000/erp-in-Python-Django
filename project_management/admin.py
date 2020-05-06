from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from utility.models import  UserProfile,Company,CompanyBranch,PredfinedPointsRule
from project_management.models import  Project,ProjectManager,Task,TaskPerformed,TaskPerformedReport,OverTime
#from hr.models import Employee_achievement


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1    

class ProjectManagerInline(admin.TabularInline):
    model = ProjectManager
    extra = 1    

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [ProjectManagerInline,TaskInline]

class TaskPerformedReportInline(admin.TabularInline):
    model = TaskPerformedReport
    extra = 1    

class TaskPerformedAdmin(admin.ModelAdmin):
    model   = TaskPerformed
    inlines = [TaskPerformedReportInline]

class OverTimeAdmin(admin.ModelAdmin):
    model = OverTime    

admin.site.register(Project, ProjectAdmin) 
admin.site.register(TaskPerformed, TaskPerformedAdmin) 
admin.site.register(OverTime, OverTimeAdmin)          