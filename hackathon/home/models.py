from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    title = models.CharField(
        max_length=1024,
        null=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comment_set.filter(parent=None)


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    question = models.ForeignKey(
        Question,
        null=False,
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.description

    def get_comments(self):
        return Comment.objects.filter(parent=self)
