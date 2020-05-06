from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User
from utility.models import  UserProfile,Company,CompanyBranch,PredfinedPointsRule,Unit,BusinessType,Tax,Vat

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile

class CompanyBranchInline(admin.StackedInline):
    model = CompanyBranch
    extra = 1     

class CompanyAdmin(admin.ModelAdmin):
    model = Company
    inlines = [CompanyBranchInline,]

class PredfinedPointsRuleAdmin(admin.ModelAdmin):
    model = PredfinedPointsRule

class UnitAdmin(admin.ModelAdmin):
    model = Unit

class BusinessTypeAdmin(admin.ModelAdmin):
    model = BusinessType

class TaxAdmin(admin.ModelAdmin):
    model = Tax

class VatAdmin(admin.ModelAdmin):
    model = Vat                


admin.site.register(UserProfile, UserProfileAdmin) 
admin.site.register(Company, CompanyAdmin) 
admin.site.register(PredfinedPointsRule, PredfinedPointsRuleAdmin) 
admin.site.register(Unit, UnitAdmin) 
admin.site.register(BusinessType, BusinessTypeAdmin) 
admin.site.register(Tax, TaxAdmin) 
admin.site.register(Vat, VatAdmin) 
