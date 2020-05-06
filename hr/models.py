from django.db import models
from django.contrib.auth.models import User
from utility.models import UserProfile,UserProfileBaseModel
# Create your models here.

class Employee(UserProfileBaseModel):
  user              = models.OneToOneField(User, related_name="Employee",blank=True, null=True,on_delete=models.CASCADE)
  fathers_name= models.CharField(max_length=255, blank=True, null=True) 
  mothers_name= models.CharField(max_length=255, blank=True, null=True) 
  home_district= models.CharField(max_length=255, blank=True, null=True) 
  #is_freedomfighter= models.CharField(max_length=32, choices=(('yes','yes'),('no','no')), blank=True) 
  spouse_occupation= models.CharField(max_length=255, blank=True, null=True) 
  spouse_district = models.CharField(max_length=255, blank=True, null=True) 
  religion= models.CharField(max_length=255, blank=True, null=True) 
  date_joining= models.DateField( blank=True, null=True)
  entry_designation= models.CharField(max_length=255, blank=True, null=True) 
  entry_scale = models.CharField(max_length=255, blank=True, null=True) 
  picture = models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)     
  archive_status = models.CharField(max_length=32, choices=(('yes','yes'),('no','no')), blank=True) 
  status = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True) 
  def get_full_name(self):
        return self.user.first_name+" "+self.user.last_name
  def __str__(self):
        return self.user.username
        
class Children(models.Model):
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='Children',on_delete=models.CASCADE)
	name = models.CharField(max_length=255, blank=True, null=True) 
	sex = models.CharField(max_length=32, choices=(('male','male'),('female','female'),('otherother','other')), blank=True) 
	dob = models.DateField( blank=True, null=True)


class DisciplinaryAction(models.Model):
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='DisciplinaryAction',on_delete=models.CASCADE)
	nature_offence = models.CharField(max_length=255, blank=True, null=True) 
	punishment = models.CharField(max_length=255, blank=True, null=True) 
	date  = models.DateField( blank=True, null=True)

class District(models.Model):
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='District',on_delete=models.CASCADE)
	name = models.CharField(max_length=255, blank=True, null=True) 
	status = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True) 

class Education(models.Model):  
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='Education',on_delete=models.CASCADE)
	name_institution= models.CharField(max_length=255, blank=True, null=True) 
	principals_subject = models.CharField(max_length=255, blank=True, null=True) 
	degree = models.CharField(max_length=255, blank=True, null=True) 
	year = models.CharField(max_length=255, blank=True, null=True) 
	division = models.CharField(max_length=255, blank=True, null=True) 

class Training(models.Model):  
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='Training',on_delete=models.CASCADE)
	title_trainin = models.CharField(max_length=255, blank=True, null=True) 
	institution  = models.CharField(max_length=255, blank=True, null=True) 
	date_from =  models.DateField( blank=True, null=True)
	date_to =  models.DateField( blank=True, null=True)
	trining_type =  models.CharField(max_length=32, choices=(('local','local'),('foreign','foreign')), blank=True) 

class Languages(models.Model):  
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='Languages',on_delete=models.CASCADE)
	languages= models.CharField(max_length=255, blank=True, null=True) 
	read  = models.CharField(max_length=255, blank=True, null=True) 
	write = models.CharField(max_length=255, blank=True, null=True) 
	speak = models.CharField(max_length=255, blank=True, null=True) 

class Address(models.Model):  
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='Address',on_delete=models.CASCADE)
	road_village= models.CharField(max_length=255, blank=True, null=True) 
	postoffice  = models.CharField(max_length=255, blank=True, null=True) 
	post_code = models.CharField(max_length=255, blank=True, null=True) 
	flat_no = models.CharField(max_length=255, blank=True, null=True) 
	police_station_thana = models.CharField(max_length=255, blank=True, null=True) 
	district = models.CharField(max_length=255, blank=True, null=True) 
	date_from = models.DateField( blank=True, null=True)
	date_from =  models.DateField( blank=True, null=True)
	address_type = models.CharField(max_length=32, choices=(('present','present'),('permanent','permanent')), blank=True) 

class Promotions(models.Model):
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='Promotions',on_delete=models.CASCADE)
	date_promotion=  models.DateField( blank=True, null=True)
	designation  = models.CharField(max_length=255, blank=True, null=True) 
	pay_scale = models.CharField(max_length=255, blank=True, null=True) 
	nature_promotion = models.CharField(max_length=255, blank=True, null=True) 


class Rest_of_recreation(models.Model):
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='Rest_of_recreation',on_delete=models.CASCADE)
	date_from =  models.DateField( blank=True, null=True)
	date_from = models.DateField( blank=True, null=True)
	coming_date = models.DateField( blank=True, null=True)

class Retirement_year(models.Model):
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='Retirement_year',on_delete=models.CASCADE)
	year=   models.DateField( blank=True, null=True)
	date  =  models.DateField( blank=True, null=True)
  
class ServiceHistory(models.Model):
	employee = models.ForeignKey(Employee, blank=True, null=True,related_name='ServiceHistory',on_delete=models.CASCADE)
	designation= models.CharField(max_length=255, blank=True, null=True)
	office_name  = models.CharField(max_length=255, blank=True, null=True)
	section = models.CharField(max_length=255, blank=True, null=True)
	date_from =  models.DateField( blank=True, null=True)
	date_from = models.DateField( blank=True, null=True)

class Employee_Achievement(models.Model):
    points_to                = models.ForeignKey(Employee, blank=True, null=True,related_name='EmployeeAchievement',on_delete=models.CASCADE)
    points_by                = models.ForeignKey(Employee, blank=True, null=True,related_name='ManagerAchievement',on_delete=models.CASCADE)
    description              = models.TextField(blank=True, null=True)
    no_of_units_completed    = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
    points_on_unit_task      =  models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
    total_units_points       = models.DecimalField(default="0.00",max_digits=12,decimal_places=2) 
    date_achivement          = models.DateField( blank=True, null=True)



	