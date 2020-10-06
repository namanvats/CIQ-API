from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, PostSerializer
from .models import Author, Post
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
 
 
class AuthorViewSet(NestedViewSetMixin, ModelViewSet):
    #model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    http_method_names = ['get','put','post','head','update','delete']
 
 
class PostViewSet(NestedViewSetMixin, ModelViewSet):
    #model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    search_fields = ["author"]
    filterset_fields = ["author"]
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get', 'post', 'head', 'update', 'patch','delete']
    