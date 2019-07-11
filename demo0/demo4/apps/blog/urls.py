from django.conf.urls import url
from . import views
from .feeds import ArticleFeed
app_name = 'blog'

urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'),
    url(r'^single/(\d+)/$', views.SingleView.as_view(), name='single'),
    url(r'^list/$', views.ListView.as_view(), name='list'),
    url(r'^addarticle/$', views.AddArticle.as_view(), name='addarticle'),
    url(r'^rss/$', ArticleFeed(), name='rss'),
    url(r'^archives/(\d+)/(\d+)/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(\d+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tags/(\d+)/$', views.TagsView.as_view(), name='tags'),
    url(r'^contact/$', views.contact, name='contact'),


]
