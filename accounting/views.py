from django.shortcuts import  get_object_or_404, render
# Create your views here.
from django.http import HttpResponseRedirect
from django.http.request import QueryDict, MultiValueDict

import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.forms import inlineformset_factory

from accounting.models import AccountYear,AccountType,Ledger,Transaction,TransactionDetails
from django import forms
from accounting.forms import  AccountYearForm,AccountTypeForm,LedgerForm,TransactionForm,TransactionDetailsForm
from django.core.mail import send_mail


from django.contrib import auth
from django.contrib.auth.models import User

from django.template import *

def index_view(request):
    return render(request, 'accounting/index.html',{})


@login_required
def accounttype_view(request):
    acctype = AccountType.objects.all()
    
    acctype_list = AccountType.objects.all().order_by('-id')

    print(acctype_list)    
     
    paginator = Paginator(acctype_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        acctype = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        acctype = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        acctype = paginator.page(paginator.num_pages)




    return render(request, 'accounting/index.html',{acctype:acctype})

@login_required
def accountyear_view(request):
    accountyear_list = AccountYear.objects.all().order_by('-id') 
    paginator = Paginator(accountyear_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        accountyear = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        accountyear = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        accountyear = paginator.page(paginator.num_pages)
    accountyearform  = AccountYearForm()    
    return render(request, 'accounting/AccountYear.html',{'accountyear_list':accountyear,'accountyearform':accountyearform})

@login_required
def accountyear_save(request):
    accountyear_form = AccountYearForm(request.POST)
    if accountyear_form.is_valid():
        accountyear = accountyear_form.save(commit=False)
        accountyear.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    