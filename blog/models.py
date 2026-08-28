from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1

    STATUS_CHOICES = (
        (STATUS_DRAFT, "Rascunho"),
        (STATUS_PUBLISHED, "Publicado"),
    )

    title = models.CharField("Título", max_length=255)
    body = models.TextField("Conteúdo", blank=True, default="")
    created_on = models.DateTimeField("Criado em", default=now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Autor",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    status = models.IntegerField("Status", choices=STATUS_CHOICES, default=STATUS_DRAFT)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
