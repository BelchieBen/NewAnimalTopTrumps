from django.db.models import fields
from django import forms
from ..models import *

class JoinRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ("code",)

    code = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Room Code'}))

