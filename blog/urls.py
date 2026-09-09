from django.urls import path

from blog.views import IndexView, PostListView

app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post_list"),
]
