from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^detail/(\d+)/$', views.detail, name='detail'),
    url('^result/(\d+)/$', views.result, name='result'),
    url('^addpoll/$', views.addpoll, name='addpoll'),
    url('^delpoll/(\d+)/$', views.delpoll, name='delpoll'),

]












