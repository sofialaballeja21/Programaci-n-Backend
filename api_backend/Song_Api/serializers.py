from rest_framework import serializers
from Song_Api.models import Song

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'