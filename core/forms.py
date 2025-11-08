from django import forms

from .models import Entry


class Shorten(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ("url",)
