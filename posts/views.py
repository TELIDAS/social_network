from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers, models, filters


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class LikeListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (AllowAny,)


class LikeCount(generics.ListAPIView):
    queryset = models.Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (AllowAny,)
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = filters.LikeFilter
