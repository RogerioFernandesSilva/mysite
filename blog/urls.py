from django.urls import path

from blog.views import PostDetail, PostList, PostListView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("lista/", PostList, name="post_list_function"),
    path("detalhe/<int:pk>/", PostDetail, name="post_detail"),
]
