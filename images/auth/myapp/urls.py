from django.conf.urls import patterns , url
from .views import *

#urlpatterns = patterns('myapp.views',
    #url(r'^list/$','list',name='list'),
    #url(r'^list1/$',list1.as_view(),name='list'),
#)

urlpatterns = [
    url(r'^list1/$',list1.as_view(),name='list'),
]