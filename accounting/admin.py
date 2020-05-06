from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User
from accounting.models import  AccountYear,AccountType,Ledger,Transaction,TransactionDetails,JournalEntry

class AccountYearAdmin(admin.ModelAdmin):
    model = AccountYear

class AccountTypeAdmin(admin.ModelAdmin):
    model = AccountType

class TransactionDetailsInline(admin.TabularInline):
    model = TransactionDetails
    extra = 1     

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('subject','ref_no','account_year','voucher_no','entry_date','post_status')
    inlines = [TransactionDetailsInline]

class JournalEntryAdmin(admin.ModelAdmin):
    model = JournalEntry  

class LedgerAdmin(admin.ModelAdmin):
    model = Ledger      
         
admin.site.register(AccountYear, AccountYearAdmin)   
admin.site.register(AccountType, AccountTypeAdmin)  
admin.site.register(Ledger, LedgerAdmin)  
admin.site.register(Transaction, TransactionAdmin)  
admin.site.register(JournalEntry, JournalEntryAdmin)
    


