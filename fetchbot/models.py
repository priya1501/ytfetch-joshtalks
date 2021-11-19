from django.db import models

# Create your models here.


class Videos(models.Model):
    title = models.CharField(null=True, blank=True,
                             max_length=500)  # Video title variable
    # Video Description variable
    description = models.CharField(null=True, blank=True, max_length=6000)
    publishingDateTime = models.DateTimeField()  # Publish date/time of the Video
    thumbnailsUrls = models.URLField()  # Thumbnail URL
    channelTitle = models.CharField(
        null=True, blank=True, max_length=500)  # Channel Title/Name
