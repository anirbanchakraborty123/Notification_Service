from django.contrib import admin
from .models import NotificationPreference ,  NotificationType

admin.site.register(NotificationPreference)
admin.site.register(NotificationType)