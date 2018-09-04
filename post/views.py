# Create your views here.
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

