from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("api/posts/", views.PostListCreateAPIView.as_view(), name="posts"),
    path("api/likes/", views.LikeListCreateAPIView.as_view(), name="likes"),
    path("api/count/", views.LikeCount.as_view(), name="like_count"),
]
