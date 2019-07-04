from django.conf.urls import url
from . import views

app_name = 'booktest'

# 绑定路由
urlpatterns = [
    # （URL， 绑定的视图函数）
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
]


