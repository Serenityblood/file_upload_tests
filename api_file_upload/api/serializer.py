from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import File


User = get_user_model()


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'id', 'author', 'new', 'review')
        read_only_fields = ('author', 'new', 'review')


class UserSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'files')

    def get_files(self, user):
        files = user.files.all()
        return FileSerializer(files, many=True).data
