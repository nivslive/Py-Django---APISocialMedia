from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Theme
from django.db.models import Sum, Count
from .serializers import ThemeSerializer

class ThemeView(APIView):
    def get(self, request, theme=None):
        if theme:
            themes = Theme.objects.prefetch_related('post_set__comment_set').filter(title=theme)
        else:
            themes = Theme.objects.prefetch_related('post_set__comment_set').all()
        
        themes = themes.annotate(comments_count=Count('post__comment')).order_by('-comments_count')
        
        serializer = ThemeSerializer(themes, many=True)
        print(serializer.data)
        return Response({'themes': serializer.data})