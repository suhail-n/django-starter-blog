from rest_framework import serializers
from django.contrib.auth.models import User

from . import models


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'
        # extra_kwargs = {'': {'required': True}}
        """
        use reference for kwargs options
        https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments

        alternatively, open up the serializer class being used (serializers.HyperlinkedModelSerializer) and look at all the "valid_kwargs" set
        """
        extra_kwargs = {
            'owner': {'required': True, 'allow_null': False}
        }


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
