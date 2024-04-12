from rest_framework import serializers
from .models import Todomodel

class TodomodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todomodel
        fields = '__all__'
 
        
# def create(self, validated_data):
#         return Todomodel.objects.create(**validated_data)
   