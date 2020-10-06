import json
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Author, Post
 
 
class AuthorSerializer(ModelSerializer):
    #posts = Post.objects.count()
    posts_count = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name' , 'posts_count')
    def get_posts_count(self, obj):
        return obj.posts.count()
 
class PostSerializer(ModelSerializer):
    author = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = ('id','title','author', 'views', 'reviews')