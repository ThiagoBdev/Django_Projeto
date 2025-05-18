from django.contrib import admin
from blog.models.post import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}




# Register your models here.
admin.site.register(Post, PostAdmin)



