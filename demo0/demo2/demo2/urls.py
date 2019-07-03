"""demo1 URL Configuration
项目根路由：用户在浏览器中输入的网址需要和路由匹配

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include



# 绑定路由
urlpatterns = [
    path('admin/', admin.site.urls),
    # （项目应用路由， 绑定应用路由下的子路由）
    url('booktest1/', include('booktest1.urls')),
]
