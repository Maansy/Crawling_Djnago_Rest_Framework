from django.shortcuts import render

# Create your views here.

#view set
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'Delete is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'Patch is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        response = {'message': 'Put is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {'message': 'Post is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)