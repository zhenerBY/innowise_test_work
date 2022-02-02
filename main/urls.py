from django.urls import path, include

from rest_framework.routers import SimpleRouter

from main.views import MessageViewSet, UsersViewSet, TicketsViewSet

router = SimpleRouter()
router.register('messages', MessageViewSet, basename='messages')
router.register('tickets', TicketsViewSet, basename='tickets')
router.register('users', UsersViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
]
