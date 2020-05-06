from django.conf.urls import url
from utility.views import dashboard_view

urlpatterns = [   
     url(r'^dashboard/', dashboard_view, name='dashboard'),
]