from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from main.models import Message, Ticket
from main.serializers import UserSerializer, MessageSerializer, TicketSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    # Set Permissions 4 New User Registration (AllowAny)
    def get_permissions(self):
        if self.action == 'register':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    # New User Registration (permission - AllowAny)
    @action(methods=['POST'], detail=False, url_path="register")
    def register(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        u = User(username=username, first_name=first_name, last_name=last_name, email=email)
        u.set_password(password)
        u.save()
        refresh = RefreshToken.for_user(u)
        res_data = {
            "user": UserSerializer(u).data,
            "token": {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }
        return Response(res_data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    # Set queryset. For staff - all, for Users - only their messages.
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(author=self.request.user.id)
        return queryset


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(creator=self.request.user.id)
        return queryset
