from django import forms

from app_main.models import ShapeRetention


class NameForm(forms.ModelForm):
    class Meta:
        model = ShapeRetention
        exclude = [""]