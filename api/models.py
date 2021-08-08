from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TimeStampMixin(models.Model):
    """
    Creates timestamps for all models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(TimeStampMixin):
    """Model definition for Article."""

    # TODO: Define fields here
    title = models.CharField(max_length=100, blank=False, default='')
    content = models.TextField(blank=True, default='')
    # on_delete will set owner to null if owner is removed
    # null=True post can exist without a user.
    # many to one. Many posts to one owner
    owner = models.ForeignKey(
        User, related_name='articles', on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.title


class Comment(TimeStampMixin):
    """Model definition for Comment."""

    # TODO: Define fields here
    owner = models.ForeignKey(
        User, related_name='comments', null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(blank=False)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return self.comment


class Tag(TimeStampMixin):
    """Model definition for Tag."""

    # TODO: Define fields here
    name = models.CharField(blank=False, null=False, max_length=30)
    articles = models.ManyToManyField(Article, related_name='tags', blank=True)
    # posts = models.ManyToManyField(
    #     Post, related_name='tags', null=True, blank=True, through='PostTag')

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.name
