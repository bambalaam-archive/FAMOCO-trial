# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from apks.models import APK
from apks.serializers import APKsSerializer

from apk_parse import apk
import os
import subprocess

# Create your views here.

def index(request):
	return HttpResponse("Hello, world!")

class ApksList(APIView):
	"""
	List all APKs, or upload a new APK
	"""

	def get(self, request, format=None):
		apks = APK.objects.all()
		serializer = APKsSerializer(apks, many=True)
		return Response(serializer.data)

class ApksDetail(APIView):
	"""
	Show specific APK by index
	"""

	def get_object(self, pk):
		try:
			return APK.objects.get(pk=pk)
		except APK.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		apk = self.get_object(pk)
		serializer = APKsSerializer(apk)
		return Response(serializer.data)


class ApksUpload(APIView):
	"""
	Upload an APK
	"""
	parser_classes = (FileUploadParser,)

	def put(self, request, filename, format='None'):
		# Setting up APK to be treated
		up_file = request.data['file']
		apkf = apk.APK(up_file.temporary_file_path())
		
		# Saving file to directory
		destination = os.getcwd()+"/apks/files/"+filename
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
		end_label = correct_line.find("icon",start_label)

		app_label = correct_line[start_label+7:end_label-2]
		
		start_icon = correct_line.find("icon=")

		app_chosen_icon = correct_line[start_icon+6:-1].replace("/","_")
		print(app_chosen_icon)

		apkf.parse_icon(os.getcwd()+"/apks/icons")

		icon_path = os.getcwd()+"/apks/icons/"+apkf.package+"/"+app_chosen_icon

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
			serializer.save()
			return Response(app_label + " has been added to the website.", status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		

"""

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""