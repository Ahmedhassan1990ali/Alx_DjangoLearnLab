from django.urls import path
from notifications.views import NotificationListAPIViewView

urlpatterns = [
    path("notifications/", NotificationListAPIViewView.as_view(), name="notifications"),
]