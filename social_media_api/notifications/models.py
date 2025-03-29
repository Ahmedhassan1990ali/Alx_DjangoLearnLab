from django.db import models
from accounts.models import CustomUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="notifications")
    actor = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="notifications_sent")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)
    verb = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target}"