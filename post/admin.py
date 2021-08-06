from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "uuid", "status", "created_date"]
    list_filter = ["status"]
    search_fields = ["title", "content"]


admin.site.register(Post, PostAdmin)
