from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = [
            "id",
            "content",
            "created_on",
            "author",
        ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = "__all__"
