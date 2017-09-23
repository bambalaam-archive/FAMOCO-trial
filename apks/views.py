# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from apks.models import APK
from apks.serializers import APKsSerializer

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

	"""
    def post(self, request, format=None):
    	serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	"""

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