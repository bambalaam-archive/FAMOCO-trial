
from rest_framework import serializers
from apks.models import APK

class APKsSerializer(serializers.ModelSerializer):
	class Meta:
		model = APK
		fields = ('id', 
				  'app_label', 
				  'app_name',
				  'version_name',
				  'version_code',
				  'icon',
				  'apk_file',
				  'date_upload')