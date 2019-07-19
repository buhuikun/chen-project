from django.conf.urls import url, include
from . import views

app_name = 'comment'

urlpatterns = [
    url(r'^addcomment/(\d+)/$', views.addcomment, name='addcomment'),

]
