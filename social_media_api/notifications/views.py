from django.shortcuts import render
from notifications.models import Notification
from notifications.serializers import NotificationSerializer
from rest_framework import generics, permissions
# Create your views here.

class NotificationListAPIViewView (generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes =[permissions.IsAuthenticated]
    def get_queryset(self):
        Notification.objects.filter(recipient=self.request.user).order_by("-timestamp")