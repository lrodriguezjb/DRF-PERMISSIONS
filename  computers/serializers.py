from rest_framework import serializers
from computers.models import Computers

class ComputersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computers
        fields = [
            'id', 'title', 'author','description', 'created_at'
        ]