from django.db import models
from django.contrib.auth.models import User

class NotificationType(models.Model):
    """
    Represents NotificationType Table with fields name and id
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class NotificationPreference(models.Model):
    """
    Represents NotificationPreference Table with fields user,notification_type,
    frequency,email,push and sms.
    """ 
    
    FREQUENCY_CHOICES = [
        ('instantly', 'Instantly'),
        ('periodically', 'Periodically'),
        ('rarely', 'Rarely'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)
    email = models.BooleanField(default=False)
    push = models.BooleanField(default=False)
    sms = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user} - {self.notification_type.name}"

    class Meta:
        unique_together = ('user', 'notification_type')
