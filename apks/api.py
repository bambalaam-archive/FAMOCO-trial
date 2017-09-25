# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

from apks.models import APK
from apks.serializers import UserSerializer, APKsSerializer
from apks.permissions import IsOwnerOrReadOnly

from apk_parse import apk
import os
import subprocess


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'apks': reverse('apk-list', request=request, format=format)
    })


class ApksList(APIView):
    """
    List all APKs, or upload a new APK
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        apks = APK.objects.all()
        serializer = APKsSerializer(apks,
                                    many=True,
                                    context={'request': request})
        return Response(serializer.data)


class ApksDetail(APIView):
    """
    Show specific APK by index
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_object(self, pk):
        try:
            return APK.objects.get(pk=pk)
        except APK.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        apk = self.get_object(pk)
        serializer = APKsSerializer(apk, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        apk = self.get_object(pk)
        apk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApksUpload(APIView):
    """
    Upload an APK
    """
    parser_classes = (FileUploadParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    cwd = os.getcwd()

    def get_apk_icons_and_path(self, apk_file, chosen_icon_filename):
        apk_file.parse_icon(self.cwd + "/apks/icons")
        icon_path = self.cwd + "/apks/icons/"
        icon_path += apk_file.package + "/" + chosen_icon_filename
        return icon_path

    def put(self, request, filename, format=None):
        # Setting up APK to be treated
        up_file = request.data['file']
        apkf = apk.APK(up_file.temporary_file_path())

        # Saving file to directory
        destination = self.cwd + "/apks/files/" + filename
        destination_file = open(destination, 'wb+')
        for chunk in up_file.chunks():
            destination_file.write(chunk)
        destination_file.close()

        # Extracting data from APK
        command = "aapt dump badging " + destination

        output = subprocess.check_output(command, shell=True).decode("utf-8")
        start = output.find("application: label")
        end = output.find("\n", start)
        correct_line = output[start:end]

        start_label = correct_line.find("label=")
        end_label = correct_line.find("icon", start_label)
        app_label = correct_line[start_label + 7:end_label - 2]

        start_icon = correct_line.find("icon=")
        app_chosen_icon = correct_line[start_icon + 6:-1].replace("/", "_")
        icon_path = self.get_apk_icons_and_path(apkf, app_chosen_icon)

        extracted_data = {}
        extracted_data['apk_file'] = destination
        extracted_data['version_name'] = apkf.get_androidversion_name()
        extracted_data['version_code'] = apkf.get_androidversion_code()
        extracted_data['icon'] = icon_path
        extracted_data["app_label"] = app_label
        extracted_data["app_name"] = apkf.package

        # Saving APK
        serializer = APKsSerializer(data=extracted_data)
        if serializer.is_valid():
            serializer.save(uploader=request.user)
            return Response(app_label + " has been added to the website.",
                            status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
