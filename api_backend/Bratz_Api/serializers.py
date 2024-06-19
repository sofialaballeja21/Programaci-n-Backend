from rest_framework import serializers
from Bratz_Api.models import Bratz

class BratzSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bratz
        #fields = ['name', 'accesorio','collection', 'picture']
        fields = '__all__'