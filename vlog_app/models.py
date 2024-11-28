from django.db import models
from django.contrib.auth.models import User
import re
# Create your models here.
class VlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    video_url = models.URLField(max_length=500)
    description = models.TextField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    published_date = models.DateField(auto_now_add=True)
    published_time = models.TimeField(auto_now_add=True)
    tags = models.ManyToManyField("Categories")

    def __str__(self):
        return self.title
    
    def embed_url(self):
        embed_regex = r"^(https:\/\/)?(www\.)?youtube\.com\/embed\/[\w-]+(\?.*)?$"
        youtube_regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"

        if re.match(embed_regex, self.video_url):
            return self.video_url
        match = re.search(youtube_regex, self.video_url)
        if match:
            video_id = match.group(1)
            return f"https://www.youtube.com/embed/{video_id}"
        return self.video_url


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=42, unique=True)

    def __str__(self):
        return self.name