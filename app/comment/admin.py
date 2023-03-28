from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from post.models import Post
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'content', 'created_at')
    list_filter = ('created_at', 'post__title')
    search_fields = ('content',)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        post_id = request.GET.get('post_id')
        if post_id:
            queryset = queryset.filter(post__id=post_id)
        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "post":
            post_id = request.GET.get('post_id')
            if post_id:
                kwargs["queryset"] = Post.objects.filter(id=post_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Comment, CommentAdmin)