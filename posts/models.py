from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="posts")


class Like(models.Model):
    LIKE_CHOICE = (("Like", "Like"), ("Unlike", "Unlike"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_time = models.DateField(auto_now_add=True)
    like_choice = models.CharField(
        max_length=100, choices=LIKE_CHOICE, default="Like", unique=True
    )
