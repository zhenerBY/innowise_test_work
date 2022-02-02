from rest_framework import serializers

from main.models import Message, Ticket


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'id',
            'text',
            'ticket',
            'author',
            'created_at',
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = 'auth.User'
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
        ]


