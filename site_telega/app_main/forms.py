from django import forms
from app_main.models import ShapeRetention


class MyForms(forms.ModelForm):
    class Meta:
        model = ShapeRetention
        fields = ["name", "number", "email", "task", ]
        labels = {'name': "Name", "number": "Number", "email": "Email", "task": "Task", }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Укажите ваше имя'}),
            'number': forms.TextInput(attrs={'placeholder': "например '@telegaBots'"}),
            'email': forms.TextInput(attrs={'placeholder': "Укажите ваш e-mail"}),
            'task': forms.Textarea(attrs={'placeholder': "Ваш вопрос",
                                          'rows': 13,
                                          'cols': 43,
                                          'style': 'resize:none;'
                                          }),

        }
