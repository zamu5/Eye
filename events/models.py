from django.db import models


class Event(models.Model):
    session_id = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    data = models.JSONField()
    timestamp = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'event_log'
        indexes = [
            models.Index(fields=['name', 'category', 'session_id'])
        ]