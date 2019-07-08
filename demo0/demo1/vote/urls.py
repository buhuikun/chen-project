from django.conf.urls import url
from . import views

app_name = 'vote'

urlpatterns = [
    url('^vindex/$', views.vindex, name='vindex'),
    url('^vdetail/(\d+)/$', views.vdetail, name='vdetail'),
    url('^result/(\d+)/$', views.result, name='result'),
    url('^login/$', views.login, name='login'),
    url('^logout/$', views.logout, name='logout'),
    url('^register/&', views.register, name='register'),
]

