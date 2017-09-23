from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'api/list/$', views.ApksList.as_view()),
    url(r'api/list/(?P<pk>[0-9]+)/$', views.ApksDetail.as_view()),
]