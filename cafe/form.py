from django import forms
from .models import editPost

class CafePost(forms.ModelForm):
    class Meta:
        model = editPost
        fields = ['title', 'body']