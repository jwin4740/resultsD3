from django.conf.urls import url
from django.contrib import admin
from . import views

# root for results route
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^task/response$', views.responseNumber, name='responseNumber'),
    url(r'^task/response/(?P<task_id>[0-9]{1})$', views.responseNumber, name='responseNumber'),
]
