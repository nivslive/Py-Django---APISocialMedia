from django.urls import path
from .views import (
    CommentView,
)

urlpatterns = [
    path('', CommentView.as_view(), name='list'),
    #path('<int:pk>/', views.comment_detail, name='detail'),
    # outras rotas aqui
]