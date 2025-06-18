from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import BlogSerializer, commentSerializer
from .models import Blog, Comment

# Create your views here.
class BlogView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs ):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
        