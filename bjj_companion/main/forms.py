from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm

from .models import *

class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = "__all__"
