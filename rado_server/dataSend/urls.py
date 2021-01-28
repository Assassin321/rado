# coding =utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Rado/$', views.getRados),
    url(r'^Boats/$', views.getBoats),
    url(r'^search/$', views.getRadoInfo),
    url(r'^download/$',views.Download),
    url(r'^test/$',views.test)
]
