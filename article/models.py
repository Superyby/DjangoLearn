from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True, null=True)

    # 外键
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='articles')
    tags = models.ManyToManyField('Tag', related_name='articles')


class Tag(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=100)


class UserExtension(models.Model):
    birthday = models.DateTimeField()
    university = models.CharField(max_length=100)
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='user_extension')


class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
