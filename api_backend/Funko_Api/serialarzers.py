from rest_framework import serializers

from Funko_Api.models import Funko, User


class FunkoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funko
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'


