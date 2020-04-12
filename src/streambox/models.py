from django.db import models

# Create your models here.
class Channel(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    channel_id = models.CharField(unique=True, max_length=50)
    thumnail_url = models.TextField(blank=True, null=True)
    published_at = models.CharField(max_length=30, blank=True, null=True)
    subscriber_num = models.IntegerField(blank=True, null=True)
    comment_num = models.IntegerField(blank=True, null=True)
    total_view = models.BigIntegerField(blank=True, null=True)
    total_video = models.IntegerField(blank=True, null=True)
    last_up = models.DateTimeField()
    category_game = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'channel'