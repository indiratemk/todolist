from django import forms
from todo.models import Task
from todo.models import Color

class TaskForm(forms.ModelForm):
    color = forms.ModelChoiceField(queryset=Color.objects)
    class Meta:
        model = Task
        fields = ('title', 'description', 'color')