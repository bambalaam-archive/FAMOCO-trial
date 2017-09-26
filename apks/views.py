# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import Http404
from apks.models import APK

from django.views import generic


def index(request):
    return render(request,
                  'index.html',
                  context={'num_apks': len(APK.objects.all()),
                           'num_users': len(User.objects.all())}
                  )


class ApkListView(generic.ListView):
    model = APK
    context_object_name = 'view_apks'
    template_name = 'apk_list.html'
    paginate_by = 10


class ApkDetailView(generic.DetailView):
    model = APK
    template_name = 'apk_detail.html'

    def apk_detail_view(self, request, pk):
        try:
            apk_id = APK.objects.get(pk=pk)
        except APK.DoesNotExist:
            raise Http404("APK does not exist")

        return render(request, self.template_name,
                      context={'apk': apk_id, })


class UserListView(generic.ListView):
    model = User
    context_object_name = 'view_users'
    template_name = 'users_list.html'
    paginate_by = 10


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user_detail.html'

    def user_detail_view(self, request, pk):
        try:
            user_id = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404("User does not exist")

        return render(request, self.template_name,
                      context={'user': user_id, })
