from django.conf.urls import url
from . import views

app_name = 'vote'

urlpatterns = [
    url('^vindex/$', views.vindex, name='vindex'),
    url('^vdetail/(\d+)/$', views.vdetail, name='vdetail'),
    url('^result/(\d+)/$', views.result, name='result'),
]

