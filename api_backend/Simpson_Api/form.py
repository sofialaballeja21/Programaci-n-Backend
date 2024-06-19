from django import forms
from Simpson_Api.models import Simpson

class SimpsonForm(forms.ModelForm):
    class Meta:
        model = Simpson
        fields = [
            'name', 
            'apellido', 
            'chapter', 
            'name_chapter', 
            'temporada'
        ]