from django.conf.urls import url
from . import views



# 绑定路由
urlpatterns = [
    # （URL， 绑定的视图函数）
    url(r'^index/$', views.index),
    url(r'^list/$', views.list),
    url(r'^detail/(\d+)/$', views.detail)
]

