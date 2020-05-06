from django import forms
from accounting.models import AccountYear,AccountType,Ledger,Transaction,TransactionDetails

from django.contrib.auth.models import User

class TransactionForm(forms.ModelForm):    
   class Meta:
        model = Transaction
        fields = ( 'trnsaction_type','subject','ref_no','account_year','voucher_no','entry_date','post_status',)

class TransactionDetailsForm(forms.ModelForm):    
    class Meta:
        model = TransactionDetails  
        fields = ( 'ledger','account_holder','description','vat','tax','debit','credit','currency',) 

class AccountYearForm(forms.ModelForm):   
    class Meta:
        model = AccountYear
        fields = ('name','slug',)

class AccountTypeForm(forms.ModelForm):   
    class Meta:
        model = AccountType
        fields = ('parent_type','name','slug',) 

class LedgerForm(forms.ModelForm):
    class Meta:
        model = Ledger
        fields = ('code','account_type','name','description','total_debit','total_credit','balance','last_update_date',  )

#00B0FF
#FF5252
#3663D5