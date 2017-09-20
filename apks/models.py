# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class APK(models.Model):
	app_label = models.CharField(max_length=200)
	app_name = models.CharField(max_length=200)
	version_name = models.CharField(max_length=200)
	version_code = models.CharField(max_length=200)
	icon = models.ImageField(upload_to='icons')
	apk_file = models.FileField(upload_to='files')
	date_upload = models.DateTimeField('date uploaded')

	def __str__(self):
		return self.app_name