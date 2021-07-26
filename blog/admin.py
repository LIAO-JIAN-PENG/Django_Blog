from django.contrib import admin
from .models import Profile, Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "status", "created_date"]
    list_filter = ["status"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Profile)
admin.site.register(Post, PostAdmin)
