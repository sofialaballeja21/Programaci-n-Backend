from rest_framework import serializers

from Simpson_Api.models import Simpson

class SimpsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simpson
        #fields = ['name', 'apellido', 'chapter', 'name_chapter', 'temporada']
        fields = '__all__'