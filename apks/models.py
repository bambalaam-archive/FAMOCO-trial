# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


class APK(models.Model):

    class Meta:
        ordering = ('date_upload',)

    app_label = models.CharField(max_length=200)
    app_name = models.CharField(max_length=200)
    version_name = models.CharField(max_length=200)
    version_code = models.CharField(max_length=200)
    icon = models.ImageField()
    apk_file = models.FileField(upload_to='apk_files/')
    date_upload = models.DateTimeField('date uploaded', auto_now_add=True)
    uploader = models.ForeignKey('auth.User',
                                 related_name='apks',
                                 on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('view-apks-detail', args=[str(self.id)])

    def __str__(self):
        return self.app_label
