import json
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Author, Post
 
 
class AuthorSerializer(ModelSerializer):
    posts_count = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name' , 'posts_count')
    def get_posts_count(self, obj):
        return obj.posts.count()
 
class PostSerializer(ModelSerializer):
    #author = serializers.SerializerMethodField()
    def validate(self, data):
        if data['views'] < 0:
            raise serializers.ValidationError("Views must be Positive")
        if data['reviews'] < 0:
            raise serializers.ValidationError("Reviews must be Positive")
        return data
    #def get_author(self,obj):
    #    return obj.first_name
    class Meta:
        model = Post
        fields = ('id','title','author', 'views', 'reviews')