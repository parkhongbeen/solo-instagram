from django.db import models
from members.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    like_user = models.ManyToManyField(
        User, through='PostLike', related_name='like_post_set'
    )
    created = models.DateTimeField(auto_now_add=True)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=True)
    image = models.ImageField(upload_to='posts/images')


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
