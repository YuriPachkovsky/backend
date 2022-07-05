from posixpath import basename
from posts.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path
router = DefaultRouter()
router.register(r'posts/text', TextPostViewSet, basename='text')
router.register(r'posts/image', TextPostViewSet, basename='image')
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'info', AuthorInfoViewSet, basename='authors_info')
router.register(r'comments', CommentsViewSet, basename='comments')
urlpatterns = router.urls
