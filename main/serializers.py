from django.contrib.auth.models import User

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


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id',
            'title',
            'creator',
            'created_at',
            'updated_at',
            'status',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]
