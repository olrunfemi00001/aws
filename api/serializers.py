from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()
