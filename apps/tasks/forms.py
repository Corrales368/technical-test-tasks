from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form for the task model
    """
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'due_date',
            'completed',
        )
        widgets = {
            'start_date': forms.DateTimeInput(
                format=('%Y-%m-%d %H:%M:%S'),
                attrs={
                    'type': 'date',
                }
            ),
        }