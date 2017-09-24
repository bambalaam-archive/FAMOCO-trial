# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import os

# Create your models here.


class APK(models.Model):
	app_label = models.CharField(max_length=200)
	app_name = models.CharField(max_length=200)
	version_name = models.CharField(max_length=200)
	version_code = models.CharField(max_length=200)
	icon = models.FilePathField(path=os.getcwd()+'/apks/icons/',recursive=True)
	apk_file = models.FilePathField(path=os.getcwd()+'/apks/files/')
	date_upload = models.DateTimeField('date uploaded')

	def __str__(self):
		return self.app_name