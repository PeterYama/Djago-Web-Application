from rest_framework import serializers
from .models import Client

# Serializers does the job of translating data to a different format
# In this case, translate the model to Json
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'address', 'age']