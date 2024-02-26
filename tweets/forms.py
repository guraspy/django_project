from django import forms
from .models import Tweet



class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet  
        fields = ["content", 'image']

    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)

# es rato mewera?
    def clean_content(self):
        content = self.cleaned_data.get("content")
        return content
