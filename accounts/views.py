from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer
    lookup_field = "id"
    permission_classes = (AllowAny,)


class NPOObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.NPOObtainPairSerializer


class UserLastLoginAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserActivitySerializer
