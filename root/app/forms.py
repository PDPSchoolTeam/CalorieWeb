from django import forms
from django.forms import ModelForm

from app.models import About


class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class ContactForm(ModelForm):
    class Meta:
        model = About
        fields = ('name', 'email', 'feedback')