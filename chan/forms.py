from django import forms
from django.forms import fields
from .models import Thread, Respone

class NewThread(forms.ModelForm):
    class Meta:
        model = Thread
        fields = [
            'name',
            'title',
            'text',
            'photo',
        ]

class Respond(forms.ModelForm):
    class Meta:
        model = Respone
        fields = [
            'name',
            'text',
            'photo',
        ]