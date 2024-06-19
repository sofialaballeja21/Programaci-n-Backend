from django import forms
from Bratz_Api.models import Bratz

class BratzForm(forms.ModelForm):
    class Meta:
        model = Bratz
        fields = [
            'name', 
            'accesorio',
            'collection', 
            'picture'
        ]