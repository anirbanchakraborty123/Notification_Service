from rest_framework import serializers
from .models import NotificationType, NotificationPreference

class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = ['id', 'name']

class NotificationPreferenceSerializer(serializers.ModelSerializer):
    notification_type = NotificationTypeSerializer()

    class Meta:
        model = NotificationPreference
        fields = ['id', 'user', 'notification_type', 'frequency', 'email', 'push', 'sms']
