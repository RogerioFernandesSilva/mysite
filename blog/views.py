# blog/views.py
from django.views.generic import ListView

from blog.models import Post


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "ultimos_posts"

    def get_queryset(self):
        return Post.objects.filter(status=Post.STATUS_PUBLISHED)[:5]


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(status=Post.STATUS_PUBLISHED)