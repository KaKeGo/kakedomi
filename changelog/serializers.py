from rest_framework import serializers

from .models import ChangeLog


MAX_BODY_LENGTH = 500

class ChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeLog
        fields = ['id', 'title', 'body', 'author', 'create_on']

class ChangeLogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeLog
        fields = ['title', 'body', 'author']

    def validate_body(self, value):
        if len(value) > MAX_BODY_LENGTH:
            raise serializers.ValidationError('This content its too long')
        return value
