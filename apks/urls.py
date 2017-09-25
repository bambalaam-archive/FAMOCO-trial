from django.conf.urls import url, include
from . import views
from . import api


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/$', api.api_root),
    url(r'^api/login/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^api/list/$', api.ApksList.as_view(),
        name="apk-list"),
    url(r'^api/list/(?P<pk>[0-9]+)/$', api.ApksDetail.as_view(),
        name="apk-detail"),
    url(r'^api/upload/(?P<filename>[^/]+)$', api.ApksUpload.as_view(),
        name="apk-upload"),
    url(r'^api/users/$', api.UserList.as_view(),
        name="user-list"),
    url(r'^api/users/(?P<pk>[0-9]+)/$', api.UserDetail.as_view(),
        name="user-detail"),
]
