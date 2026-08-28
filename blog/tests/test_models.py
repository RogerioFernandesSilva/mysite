import pytest

from blog.factories import PostFactory
from blog.models import Post


@pytest.mark.django_db
class TestPostModel:
    def test_create_post(self):
        post = PostFactory()
        assert isinstance(post, Post)
        assert post.pk is not None

    def test_post_str_returns_title(self):
        post = PostFactory(title="Meu primeiro post")
        assert str(post) == "Meu primeiro post"

    def test_post_default_status_is_draft(self):
        post = PostFactory()
        assert post.status == Post.STATUS_DRAFT

    def test_post_has_author(self):
        post = PostFactory()
        assert post.author is not None
        assert post.author.pk is not None

    def test_post_created_on_is_set(self):
        post = PostFactory()
        assert post.created_on is not None
