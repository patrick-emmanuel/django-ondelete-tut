from rest_framework import serializers

from comment.serializers import CommentSerializer
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'comments')
