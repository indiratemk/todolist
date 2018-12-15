from django.contrib import admin
from django.conf.urls import url, include
from todo import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/', views.home, name='main_page'),
    url(r'^add/', views.add, name='add'),
    url(r'^update/(?P<id>\d+)/$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^complete/(?P<id>\d+)/$', views.task_complete, name='task-complete'),
    url(r'^search/$', views.search, name='search'),
    url(r'^$', views.login, name='login'),
    url(r'^sign_in/', views.sign_in, name='sign_in'),
    url(r'^logout/$', views.sign_out, name='sign_out')
]
