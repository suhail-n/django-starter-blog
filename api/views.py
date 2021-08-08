from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers import ArticleSerializer, CommentSerializer, TagSerializer, UserSerializer
from api.models import Article, Comment, Tag

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=True)
    def comments(self, request, pk=None):
        """
        using action to add extra routes to viewset
        /articles/10/comments/ - grab all comments for this article

        """
        article = Article.objects.get(pk=pk)
        # ordered by latested created date
        article_comments = article.comments.order_by('-created_at')
        return Response(self.get_serializer(article_comments, many=True).data)


class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
