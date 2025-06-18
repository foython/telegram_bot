from rest_framework import serializers
from .models import Blog, Comment



class BlogSerializer(serializers.ModelSerializer):     
    
    class Meta:
        model = Blog
        fields = ('id', 'topic', 'title', 'text', 'author')
        read_only_fields = ('id',)               
        
        
class commentSerializer(serializers.ModelSerializer):     
    
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'blog')
        read_only_fields = ('id',) 
    