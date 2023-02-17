from django import forms
from polls.models import *

class CommentForm(forms.ModelForm):
    title = forms.TextInput()
    body = forms.TextInput()
    class Meta:
        model = Comments
        fields = ['title', 'body']