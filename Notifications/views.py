from rest_framework import generics
from .models import NotificationType, NotificationPreference
from .serializers import NotificationTypeSerializer, NotificationPreferenceSerializer

class NotificationTypeListCreateView(generics.ListCreateAPIView):
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer

class NotificationPreferenceListCreateView(generics.ListCreateAPIView):  
    queryset = NotificationPreference.objects.all()
    serializer_class = NotificationPreferenceSerializer

class NotificationPreferenceDetailView(generics.RetrieveUpdateAPIView):  
    queryset = NotificationPreference.objects.all()
    serializer_class = NotificationPreferenceSerializer
