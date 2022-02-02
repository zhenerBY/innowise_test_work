from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from main.models import Message, Ticket
from main.serializers import UserSerializer, MessageSerializer, TicketSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]
