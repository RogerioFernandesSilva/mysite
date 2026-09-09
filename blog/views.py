from django.views.generic import ListView, TemplateView

from blog.models import Post


class IndexView(TemplateView):
    template_name = "blog/index.html"


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(status=Post.STATUS_PUBLISHED)