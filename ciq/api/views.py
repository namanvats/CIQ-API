from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, PostSerializer
from .models import Author, Post
from rest_framework.response import Response
#from rest_framework_extensions.mixins import NestedViewSetMixin
 
 
class AuthorViewSet(ModelViewSet):
    #model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    http_method_names = ['get','put','post','head','update']
 
 
class PostViewSet(ModelViewSet):
    #model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    http_method_names = ['get', 'post', 'head', 'update', 'patch','delete']