from django.db import models
from utility.models import BaseModel,UserProfile
from hr.models import Employee

# Create your models here.
class AccountYear(models.Model):
	name         = models.CharField(max_length=255, blank=True, null=True)
	start_date   = models.DateField( blank=True, null=True)
	end_date     = models.DateField( blank=True, null=True)
	slug         = models.CharField(max_length=255, blank=True, null=True)
	def __str__(self):
	    return self.name
"""
accont_choice =     Balance Sheet Accounts
        				         Assets
        				                Cash            
        				                Account Receiveable
        				                Equipment
        				                Inventory
        				                Prepaid Expenses
        				         Liablities
        				                Accounts Payable
        				                Accured Expenses
        				                Notes Payable  
        				                Unearned Revenue
        				                Deferred Taxes
        				         Owner's Equity   
        				               Capital
        				               Retained Earnings  
        				      Income Statements Accounts 
          				          Revenue 
          				               Income                 
          				          Expense
          				               Salaries
          				               Selling Expenses
          				               Depreciation
          				               Rent
          				               Interest Expense
"""        
class AccountType(models.Model):#chart of account
    parent_type  = models.ForeignKey('self', blank=True, null=True, default=None, related_name='prev_item',on_delete=models.CASCADE)
    name         = models.CharField(max_length=255, blank=True, null=True)
    slug         = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name

class Ledger(models.Model):
    code             = models.CharField(max_length=255, blank=True, null=True)
    account_type     = models.ForeignKey(AccountType, blank=True, null=True,on_delete=models.CASCADE)     
    name             = models.CharField(max_length=255, blank=True, null=True)
    description      = models.TextField(blank=True, null=True)
    total_debit      = models.DecimalField(verbose_name="Total Debit",default="0.00",max_digits=12,decimal_places=2)
    total_credit     = models.DecimalField(verbose_name="Total Credit",default="0.00",max_digits=12,decimal_places=2)
    balance          = models.DecimalField(verbose_name="Balance",default="0.00",max_digits=12,decimal_places=2)
    last_update_date = models.DateField( blank=True, null=True)  
    def __str__(self):
        return self.name


class Transaction(BaseModel):
    trnsaction_type = models.CharField(max_length=32, choices=(('General','General'),('POS','POS')), blank=True)  
    subject         = models.CharField(max_length=255, blank=True, null=True)
    ref_no          = models.CharField(max_length=255, blank=True, null=True)
    account_year    = models.ForeignKey(AccountYear, blank=True, null=True,on_delete=models.CASCADE)
    voucher_no      = models.CharField(max_length=255, blank=True, null=True)
    entry_date      = models.DateField( blank=True, null=True)   
    post_status     = models.CharField(max_length=32, choices=(('pending','pending'),('posted','posted')), blank=True) 
    def __str__(self):
        return self.subject

class TransactionDetails(models.Model):
    transaction    = models.ForeignKey(Transaction, blank=True, null=True,on_delete=models.CASCADE)
    ledger         = models.ForeignKey(Ledger, blank=True, null=True,on_delete=models.CASCADE)
    account_holder = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)
    description    = models.TextField(blank=True, null=True)
    #quantity      = models.DecimalField(verbose_name="Quantity (Optional)",default="0.00",max_digits=12,decimal_places=2)
    #rate          = models.DecimalField(verbose_name="Rate (Optional)",default="0.00",max_digits=12,decimal_places=2)
    #amount        = models.DecimalField(verbose_name="Credit",default="0.00",max_digits=12,decimal_places=2)
    vat            = models.DecimalField(verbose_name="vat(%)",default="0.00",max_digits=12,decimal_places=2)
    tax            = models.DecimalField(verbose_name="tax(%)",default="0.00",max_digits=12,decimal_places=2)
    debit          = models.DecimalField(verbose_name="Debit",default="0.00",max_digits=12,decimal_places=2)
    credit         = models.DecimalField(verbose_name="Credit",default="0.00",max_digits=12,decimal_places=2)
    currency       = models.CharField(max_length=255, blank=True, null=True)
    #entry_type     = models.CharField(max_length=32, choices=(('debit','debit'),('credit','credit')), blank=True)
   
    

class JournalEntry(models.Model):
   transaction  = models.ForeignKey(Transaction, blank=True, null=True,on_delete=models.CASCADE)
   ref_no       = models.CharField(max_length=255, blank=True, null=True)
   debit        = models.DecimalField(verbose_name="Debit",default="0.00",max_digits=12,decimal_places=2)
   credit       = models.DecimalField(verbose_name="Credit",default="0.00",max_digits=12,decimal_places=2)
   currency     = models.CharField(max_length=255, blank=True, null=True)
   entry_date   = models.DateField( blank=True, null=True)   
   def __str__(self):
        return self.transaction.subject
