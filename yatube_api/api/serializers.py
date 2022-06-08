from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.shortcuts import get_object_or_404

from posts.models import Comment, Follow, Group, Post, User

NOT_FOLLOW_YOURSELF_MESSAGE = 'Error. You cannot follow yourself'
ALREADY_FOLLOW_MESSAGE = 'Error. You already follow this user'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()
    user = serializers.SlugRelatedField(
        slug_field='username',
        required=False,
        default=serializers.CurrentUserDefault(),
        queryset=queryset
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=queryset
    )

    def validate(self, data):
        author = get_object_or_404(User, username=data.get('following'))
        user = data.get('user')
        if author == user:
            raise serializers.ValidationError(NOT_FOLLOW_YOURSELF_MESSAGE)
        return data

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following'],
            message=ALREADY_FOLLOW_MESSAGE
        )]
