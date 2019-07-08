from django.conf.urls import url
from . import views

app_name = 'booktest'

# 绑定路由
urlpatterns = [
    # （URL， 绑定的视图函数）
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^deletebook/(\d+)/$', views.deletebook, name='deletebook'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout')

]
