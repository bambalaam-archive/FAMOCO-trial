from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = format_suffix_patterns([
    url(r'^$', views.index, name='index'),
    url(r'^api/$', views.api_root),
    url(r'^api/list/$', views.ApksList.as_view(),name="apk-list"),
    url(r'^api/list/(?P<pk>[0-9]+)/$', views.ApksDetail.as_view(),name="apk-detail"),
    url(r'^api/upload/(?P<filename>[^/]+)$', views.ApksUpload.as_view(), name="apk-upload"),
    url(r'^api/users/$', views.UserList.as_view(), name="user-list"),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="user-detail"),
])

urlpatterns += [
	url(r'^api/login/', include('rest_framework.urls', namespace='rest_framework')),
]