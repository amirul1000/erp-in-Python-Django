from django.contrib.auth.models import User
from accounting.models import AccountYear,AccountType,Ledger,Transaction,TransactionDetails

from rest_framework import serializers

class AccountYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountYear
        fields = ('name', 'start_date', 'end_date', 'slug')

class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = ('id','parent_type','name','slug')        