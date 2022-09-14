from django import forms
from django.forms import fields

from .models import *


class NewThread(forms.ModelForm):

    class Meta:
        model = Thread
        fields = [
            'poster',
            'subject',
            'content',
            'file',
        ]


class NewReply(forms.ModelForm):

    class Meta:
        model = Reply
        fields = [
            'poster',
            'content',
            'file',
        ]
