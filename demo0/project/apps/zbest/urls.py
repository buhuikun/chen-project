from django.conf.urls import url, include
from .views import *


app_name = 'zbest'


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^checkuser/$', checkuser, name='checkuser'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^list/(\d+)/$', ListView.as_view(), name='list'),
    url(r'^detail/(\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^center/(\d+)/$', center, name='center'),
    url(r'^myorder/$', myorder, name='myorder'),
    url(r'^cart/$', cart, name='cart'),
    url(r'^buy/(\d+)/$', buy, name='buy'),
    url(r'^addcart/$', addcart, name='addcart'),
    url(r'^order/(\d+)/$', order, name='order'),
    url(r'^createorder/$', createorder, name='createorder'),
    url(r'^delcart/(\d+)/$', delcart, name='delcart'),
    url(r'^createcartorder/$', createcartorder, name='createcartorder'),
    url(r'^confirm/(\d+)/$', confirm, name='confirm'),
    url(r'^orderxq/(\d+)/$', orderxq, name='orderxq'),
    url(r'^myprod/$', myprod, name='myprod'),




]