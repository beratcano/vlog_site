from django import forms
from .models import VlogPost

class VlogPostForm(forms.ModelForm):
    class Meta:
        model = VlogPost
        fields = ["title", 
                  "video_url", 
                  "description", 
                  "tags"]