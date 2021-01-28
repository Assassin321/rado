# coding =utf-8

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.getSeaRank),
    url(r'^warn/$', views.WarningInfo),
   # url(r'^download/$',views.Download)
]