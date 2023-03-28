from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'comment_count')
    list_filter = ('created_at',)
    search_fields = ('title',)
    def comment_count(self, obj):
        return obj.comment_count  # Retorna o atributo comment_count do objeto Post
    comment_count.admin_order_field = 'comment_count'
    comment_count.short_description = 'Comentários'

admin.site.register(Post, PostAdmin)
