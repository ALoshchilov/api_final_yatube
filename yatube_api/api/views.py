# TODO:
# Отправить на ревью;
# Дождаться обратной связи;
# Внести изменения согласно обратной связи;

from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import AuthorOrReadOnly, ReadOnly
from api.serializers import (
    CommentSerializer, GroupSerializer, FollowSerializer, PostSerializer
)
from posts.models import Comment, Follow, Group, Post, User

SAFE_METHODS = ('retrieve', 'list',)
BAD_REQUEST_MESSAGE = 'Error. Bad request. Param "Following" not found or None'
NOT_FOLLOW_YOURSELF_MESSAGE = 'Error. You cannot follow yourself'
ALREADY_FOLLOW_MESSAGE = 'Error. You already follow {author}'


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return self.queryset.filter(post=post)

    def perform_create(self, serializer, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(
            author=self.request.user,
            post=post
        )

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        author_nick = self.request.data.get('following')
        if not author_nick:
            raise ValidationError(BAD_REQUEST_MESSAGE)
        author = get_object_or_404(User, username=author_nick)
        follow = Follow.objects.filter(
            user=self.request.user, following=author
        )
        if follow:
            raise ValidationError(
                ALREADY_FOLLOW_MESSAGE.format(author=author.username)
            )
        if author == self.request.user:
            raise ValidationError(NOT_FOLLOW_YOURSELF_MESSAGE)
        serializer.save(user=self.request.user, following=author)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return (ReadOnly(),)
        return super().get_permissions()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return (ReadOnly(),)
        return super().get_permissions()
