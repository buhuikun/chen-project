from django.conf.urls import url
from . import views
app_name = 'blog'


urlpatterns = [
    url('^$', views.index, name='index'),
    url('^base/$', views.base, name='base'),

]






