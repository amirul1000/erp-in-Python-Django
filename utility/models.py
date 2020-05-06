from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from utility.country_codes import COUNTRY_CHOICES

# Create your models here.
class BaseModel(models.Model):
   created_on = models.DateTimeField(auto_now_add=True, null=True,blank=True)
   modified_on = models.DateTimeField(auto_now=True)
   created_by = models.ForeignKey(settings.AUTH_USER_MODEL,  related_name='%(class)s_createdby', null=True,blank=True, on_delete=models.CASCADE)
   modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_modifiedby', null=True,blank=True, on_delete=models.CASCADE)
   class Meta:
       abstract = True
    
class AddressBaseModel(models.Model):
  address1          = models.CharField(max_length=255, blank=True, null=True) 
  address2          = models.CharField(max_length=255, blank=True, null=True) 
  country           = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
  state             = models.CharField(max_length=255, blank=True, null=True) 
  city              = models.CharField(max_length=255, blank=True, null=True) 
  zip_code          = models.CharField(max_length=255, blank=True, null=True) 

  class Meta:
     abstract = True


class UserProfile(models.Model):
    user              = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, primary_key=True) 
    first_name        = models.CharField(max_length=255, blank=True, null=True) 
    last_name        = models.CharField(max_length=255, blank=True, null=True) 
    gender            = models.CharField(max_length=32, choices=(('Male','Male'),('Female','Female'),('Other','Other')), blank=True)     
    date_of_birth     = models.DateField( blank=True, null=True)
    nationalid= models.CharField(max_length=255, blank=True, null=True) 
    blood_group= models.CharField(max_length=255, blank=True, null=True) 
    marital_status= models.CharField(max_length=255, blank=True, null=True) 
    name_spouse= models.CharField(max_length=255, blank=True, null=True)
    email             = models.CharField(max_length=255, blank=True, null=True) 
    cell_phone        = models.CharField(max_length=255, blank=True, null=True) 
    land_phone        = models.CharField(max_length=255, blank=True, null=True) 
    country           = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    state             = models.CharField(max_length=255, blank=True, null=True) 
    city              = models.CharField(max_length=255, blank=True, null=True) 
    zip_code          = models.CharField(max_length=255, blank=True, null=True) 
    permanent_address = models.TextField(blank=True, null=True)
    about             = models.TextField(blank=True, null=True)
    contact_details   = models.TextField(blank=True, null=True)
    latitude          = models.CharField(max_length=512, blank=True, null=True)  
    longitude         = models.CharField(max_length=512, blank=True, null=True)  
    def get_full_name(self):
           return self.user.first_name+" "+self.user.last_name
    def __str__(self):
        return self.user.username

User.profile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])


class UserProfileBaseModel(models.Model):       
    first_name        = models.CharField(max_length=255, blank=True, null=True) 
    last_name         = models.CharField(max_length=255, blank=True, null=True) 
    gender            = models.CharField(max_length=32, choices=(('Male','Male'),('Female','Female'),('Other','Other')), blank=True)     
    date_of_birth     = models.DateField( blank=True, null=True)
    nationalid        = models.CharField(max_length=255, blank=True, null=True) 
    blood_group       = models.CharField(max_length=255, blank=True, null=True) 
    marital_status    = models.CharField(max_length=255, blank=True, null=True) 
    name_spouse       = models.CharField(max_length=255, blank=True, null=True)
    email             = models.CharField(max_length=255, blank=True, null=True) 
    cell_phone        = models.CharField(max_length=255, blank=True, null=True) 
    land_phone        = models.CharField(max_length=255, blank=True, null=True) 
    country           = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    state             = models.CharField(max_length=255, blank=True, null=True) 
    city              = models.CharField(max_length=255, blank=True, null=True) 
    zip_code          = models.CharField(max_length=255, blank=True, null=True) 
    permanent_address = models.TextField(blank=True, null=True)
    about             = models.TextField(blank=True, null=True)
    contact_details   = models.TextField(blank=True, null=True)
    latitude          = models.CharField(max_length=512, blank=True, null=True)  
    longitude         = models.CharField(max_length=512, blank=True, null=True)  
    class Meta:
       abstract = True
       
class Company(models.Model):
  name                   =  models.CharField(max_length=255, blank=True, null=True) 
  description            = models.TextField(blank=True, null=True)
  email                  = models.CharField(max_length=255, blank=True, null=True) 
  cell_phone             = models.CharField(max_length=255, blank=True, null=True) 
  land_phone             = models.CharField(max_length=255, blank=True, null=True) 
  country                = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
  state                  = models.CharField(max_length=255, blank=True, null=True) 
  city                   = models.CharField(max_length=255, blank=True, null=True) 
  zip_code               = models.CharField(max_length=255, blank=True, null=True) 
  about                  = models.TextField(blank=True, null=True)
  contact_details        = models.TextField(blank=True, null=True)
  latitude               = models.CharField(max_length=512, blank=True, null=True)  
  longitude              = models.CharField(max_length=512, blank=True, null=True)  
  year_established       =  models.DateField( blank=True, null=True)
  total_employees        =  models.CharField(max_length=255, blank=True, null=True) 
  business_type          =  models.CharField(max_length=255, blank=True, null=True)  
  main_products          =  models.CharField(max_length=255, blank=True, null=True) 
  total_annual_revenue   =  models.CharField(max_length=255, blank=True, null=True) 
  url                    =  models.CharField(max_length=255, blank=True, null=True) 
  social_link            =  models.CharField(max_length=255, blank=True, null=True) 



class CompanyBranch(models.Model):
  company                = models.ForeignKey(Company, blank=True, null=True,on_delete=models.CASCADE)
  name                   =  models.CharField(max_length=255, blank=True, null=True) 
  description            = models.TextField(blank=True, null=True)
  email                  = models.CharField(max_length=255, blank=True, null=True) 
  cell_phone             = models.CharField(max_length=255, blank=True, null=True) 
  land_phone             = models.CharField(max_length=255, blank=True, null=True) 
  country                = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
  state                  = models.CharField(max_length=255, blank=True, null=True) 
  city                   = models.CharField(max_length=255, blank=True, null=True) 
  zip_code               = models.CharField(max_length=255, blank=True, null=True) 
  about                  = models.TextField(blank=True, null=True)
  contact_details        = models.TextField(blank=True, null=True)
  latitude               = models.CharField(max_length=512, blank=True, null=True)  
  longitude              = models.CharField(max_length=512, blank=True, null=True)  
  year_established       =  models.DateField( blank=True, null=True)
  total_employees        =  models.CharField(max_length=255, blank=True, null=True) 
  business_type          =  models.CharField(max_length=255, blank=True, null=True)  
  main_products          =  models.CharField(max_length=255, blank=True, null=True) 
  total_annual_revenue   =  models.CharField(max_length=255, blank=True, null=True) 
  url                    =  models.CharField(max_length=255, blank=True, null=True) 
  social_link            =  models.CharField(max_length=255, blank=True, null=True) 


class PredfinedPointsRule(BaseModel):
    units_points         = models.DecimalField(default="0.00",max_digits=12,decimal_places=2) 
    task_description     = models.TextField(blank=True, null=True)
    comments             = models.TextField(blank=True, null=True)

class TaskUnitsPointsBaseModel(models.Model):
  total_units_task           =  models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
  unit_task_description      =  models.TextField(blank=True, null=True)
  points_on_unit_task        =  models.DecimalField(default="0.00",max_digits=12,decimal_places=2)

class Unit(models.Model):
  name                   =  models.CharField(max_length=255, blank=True, null=True) 
  description            = models.TextField(blank=True, null=True)
  def __str__(self):
        return self.name
   
       
class BusinessType(models.Model):
  name                   =  models.CharField(max_length=255, blank=True, null=True) 
  description            = models.TextField(blank=True, null=True)
  def __str__(self):
        return self.name
        
class Tax(models.Model):
    business_type = models.ForeignKey(BusinessType, blank=True, null=True,related_name='TaxBusinessType',on_delete=models.CASCADE) 
    tax = models.FloatField(verbose_name=("Tax(%)"), blank=True,null=True)
    def __unicode__(self):
        return self.name

class Vat(models.Model):
    business_type = models.ForeignKey(BusinessType, blank=True, null=True,related_name='VatBusinessType',on_delete=models.CASCADE) 
    vat = models.FloatField(verbose_name=("Vat(%)"),blank=True,null=True)
    def __unicode__(self):
        return str(self.vat)


class ScheduleBaseModel(models.Model):
  subject            = models.CharField(max_length=255,blank=True, null=True)
  description        = models.TextField(blank=True, null=True)
  date_from          = models.DateField( blank=True, null=True)
  time_from          = models.TimeField( blank=True, null=True)
  date_to            = models.DateField( blank=True, null=True)
  time_to            = models.TimeField( blank=True, null=True)
  