from django.views.generic import ListView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(status=Post.STATUS_PUBLISHED)
