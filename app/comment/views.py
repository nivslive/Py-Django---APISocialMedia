from django.shortcuts import render

from .models import Comment

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from .serializers import CommentSerializer

class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'), 
    #         'completed': request.data.get('completed'), 
    #         'user': request.user.id
    #     }
    #     serializer = TodoSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)