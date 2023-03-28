from django.db import models
from post.models import Post
from theme.models import Theme
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
    class Meta:
        db_table = 'comment'