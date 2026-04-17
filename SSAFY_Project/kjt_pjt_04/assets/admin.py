from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "asset_id", "author", "created_at", "updated_at")
    list_filter = ("asset_id", "author")
    search_fields = ("title", "content", "author")
