from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class BlogPost(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    category = models.ForeignKey('BlogPostCategory', null=True, on_delete=models.SET_NULL, )


class BlogPostImage(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='blog')
    blogpost = models.ForeignKey('BlogPost', on_delete=models.CASCADE)


class BlogPostCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Article(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    category = models.ForeignKey('ArticleCategory', null=True, on_delete=models.SET_NULL, )


class ArticleImage(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='blog')
    article = models.ForeignKey('Article', on_delete=models.CASCADE)


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class QuestionCategory(models.Model):
    name = models.CharField()


class Question(models.Model):
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    contents = models.CharField(max_length=255)
    ans_a = models.CharField()
    ans_b = models.CharField()
    ans_c = models.CharField()
    ans_d = models.CharField()
    correct = models.CharField()


# class Profile(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     bio = models.TextField(max_length=500, blank=True)

class Result(models.Model):
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    amount = models.IntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
