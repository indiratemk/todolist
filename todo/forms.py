from django import forms
from todo.models import Task
from todo.models import Color
from todo.models import User

class TaskForm(forms.ModelForm):
    color = forms.ModelChoiceField(queryset=Color.objects)
    user = forms.ModelChoiceField(queryset=User.objects)
    class Meta:
        model = Task
        fields = ('title', 'description', 'color', 'user')