from django import forms
from django.forms import fields

from .models import Respone, Thread


class NewThread(forms.ModelForm):
    """Form used to creating new threads."""

    class Meta:
        model = Thread
        fields = [
            'name',
            'title',
            'text',
            'photo',
        ]


class Respond(forms.ModelForm):
    """Form used for replying to threads."""

    class Meta:
        model = Respone
        fields = [
            'name',
            'text',
            'photo',
        ]
