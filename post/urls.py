from django.urls import path
from rest_framework.routers import DefaultRouter

from comment.views import AddCommentView, DeleteCommentView
from post.views import PostViewSet

app_label = 'post'

router = DefaultRouter(trailing_slash=False)

router.register(r'posts', PostViewSet)


urlpatterns = [
    path('posts/<int:post_id>/comments', AddCommentView.as_view(), name='add-comment'),
    path('comments/<int:pk>', DeleteCommentView.as_view(), name='delete-comment')
] + router.urls
