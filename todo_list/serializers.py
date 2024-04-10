from rest_framework import serializers
from . models import Todomodel
class TodomodelSerializer(serializers.Serializer):
     class Meta:
        model=Todomodel
        fields = '__all__' 