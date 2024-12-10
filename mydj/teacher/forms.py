from main.models import Task, Lesson, Feedback
from django.forms import ModelForm, TextInput, DateInput, DateField

class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'deadline']

        widgets = {
            "Description":TextInput(attrs={
                'placeholder': 'Your description'
            }),
            "Deadline": DateInput(attrs={
                'placeholder': 'Your deadline'
            })
        }

class Lessonform(ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'date']

        widgets = {
            "Subject":TextInput(attrs={
                'placeholder': 'Your subject'
            }),
            "Date of lessons":DateInput(attrs={
                'placeholder': 'Date of lesson'
            })
        }