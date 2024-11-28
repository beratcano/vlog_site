from django import forms
from .models import VlogPost
import re

class VlogPostForm(forms.ModelForm):
    class Meta:
        model = VlogPost
        fields = ["title", 
                  "video_url", 
                  "description", 
                  "tags"]
    
    def clean_video_url(self):
        video_url = self.cleaned_data.get('video_url')
        youtube_regex = r"^(https:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)[\w-]+(\?.*)?$"
        embed_regex = r"^(https:\/\/)?(www\.)?(youtube\.com\/embed\/)[\w-]+(\?.*)?$"

        if re.match(embed_regex, video_url) or re.match(youtube_regex, video_url): #type:ignore
            return video_url  
        raise forms.ValidationError(f"{video_url} is not a valid YouTube URL.")