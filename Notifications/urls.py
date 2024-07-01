from django.urls import path
from .views import NotificationTypeListCreateView, NotificationPreferenceListCreateView, NotificationPreferenceDetailView

urlpatterns = [
    path('notification-types/', NotificationTypeListCreateView.as_view(), name='notification-type-list-create'),
    path('notification-preferences/', NotificationPreferenceListCreateView.as_view(), name='notification-preference-list-create'),
    path('notification-preferences/<int:pk>/', NotificationPreferenceDetailView.as_view(), name='notification-preference-detail'),
]
