from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddBlog(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
