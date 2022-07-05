from rest_framework import viewsets
from rest_framework.response import Response
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from posts.serializer import *
from django.views.decorators.cache import cache_page
import time

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']
    ordering_fields = ['username', 'email']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AuthorInfoViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorInfoSerializer
    queryset = AuthorInfo.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['birthday', 'country']
    ordering_fields = ['birthday', 'country']

class TextPostViewSet(viewsets.ModelViewSet):
    serializer_class = TextPostSerializer
    queryset = TextPosts.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title']
    ordering_fields = ['title']

class ImagePostViewSet(viewsets.ModelViewSet):
    serializer_class = ImagePostSerializer
    queryset = ImagePost.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title']
    ordering_fields = ['title']

class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['create_at', 'owner']
    ordering_fields = ['create_at', 'owner']
