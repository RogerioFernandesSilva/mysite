from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ("title", "body")
