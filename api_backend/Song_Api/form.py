from django import forms

from Song_Api.models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            'name_song',
            'duration',
            'name_autor',
            'name_discografica',
            'genero',
            'id_song'
        ]