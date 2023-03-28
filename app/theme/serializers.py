from rest_framework import serializers
from .models import Theme
#from post.serializers import PostSerializer
from comment.serializers import CommentSerializer


class ThemeSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Theme
        fields = '__all__'

    def get_posts(self, obj):
        posts = obj.post_set.all()
        posts_data = []
        for post in posts:
            comments = post.comment_set.all()
            comments_data = CommentSerializer(comments, many=True).data

            post_data = {
                'id': post.id,
                'title': post.title,
                'description': post.description,
                'created_at': post.created_at,
                'comments': comments_data,
                'comments_count': len(comments_data)
            }
            
            posts_data.append(post_data)
        return posts_data