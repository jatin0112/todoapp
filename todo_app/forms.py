from django import forms
from .models import ReminderThings

class ReminderForm(forms.ModelForm):
    class Meta:
        model = ReminderThings 
        fields = ['title']
