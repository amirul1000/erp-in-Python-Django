from django.conf.urls import url

from restapp import views


urlpatterns = [
   url(r'^user/', views.UserList.as_view()),
   url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]