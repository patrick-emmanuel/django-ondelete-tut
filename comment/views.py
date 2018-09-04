# Create your views here.
from rest_framework.generics import CreateAPIView, get_object_or_404, DestroyAPIView, UpdateAPIView

from comment.models import Comment
from comment.serializers import CommentSerializer
from post.models import Post


class AddCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(post=post)


class DeleteCommentView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpdateCommentView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
