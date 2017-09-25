
from rest_framework import serializers
from apks.models import APK
from django.contrib.auth.models import User


class APKsSerializer(serializers.HyperlinkedModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')

    class Meta:
        model = APK
        fields = ('id',
                  'url',
                  'app_name',
                  'app_label',
                  'version_name',
                  'version_code',
                  'icon',
                  'apk_file',
                  'date_upload',
                  'uploader',
                  )

    def create(self, validated_data):
        """
        Create and return a new 'APK' instance, given the validated data.
        """
        return APK.objects.create(**validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    apks = serializers.HyperlinkedRelatedField(many=True,
                                               view_name="apk-detail",
                                               read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'apks')
