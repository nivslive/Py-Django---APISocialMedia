from django.db import models
from theme.models import Theme
class Post(models.Model):
 
    # fields of the model
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def comment_count(self):
        from comment.models import Comment  # importação aqui
        return Comment.objects.filter(post=self).count()
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'post'