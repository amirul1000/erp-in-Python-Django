from django.conf.urls import url
from django.views.generic import TemplateView
from accounting.views  import  accountyear_view,accountyear_save,index_view,accounttype_view

from accounting import views
#from accounting import rest_api_views


urlpatterns = [
  
    url(r'^index/', index_view, name='accounting_home'),
    url(r'^accounttype/', accounttype_view, name='accounttype'),
    url(r'^accountyear/', accountyear_view, name='accountyear'),
    url(r'^accountyear_save/', accountyear_save, name='accountyear_save'),

   

]