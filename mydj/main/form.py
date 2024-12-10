from .models import Feedback
from django.forms import ModelForm, TextInput

class Feedbackform(ModelForm):
    class Meta:
        model = Feedback
        fields = ['topic', 'description']

        widgets = {
            "Topic":TextInput(attrs={
                'placeholder': 'Your topic'
            }),
            "Description": TextInput(attrs={
                'placeholder': 'Your description'
            })
        }

