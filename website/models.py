from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Blog_post(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL,)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Article(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL,)

class Article_category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Question_category(models.Model):
    name = models.CharField()

class Question(models.Model):
    category = models.ForeignKey(Question_category, on_delete=models.CASCADE)
    contents = models.CharField(max_length=255)
    ans_a = models.CharField()
    ans_b = models.CharField()
    ans_c = models.CharField()
    ans_d = models.CharField()
    correct = models.CharField()

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
class Result(models.Model):
    category=models.ForeignKey(Question_category, on_delete=models.CASCADE)
    amount=models.IntegerField()
    user=models.ForeignKey(Profile,null=True,on_delete=models.SET_NULL)





