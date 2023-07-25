import base64
import io
import random

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

import matplotlib.pyplot as plt

from .forms import *


def main(request):
    return render(request, 'layout.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'serv.html')


class RegisterUserView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, 'register_user.html', context={'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            User.objects.create(username=data.get('username'), password=data.get('password'),
                                first_name=data.get('first_name'), last_name=data.get('last_name'),
                                email=data.get('email'))

            msg = 'użytkownik zarejestrowany pomyslnie!'
            return render(request, 'home.html', {'msg': msg})
        else:
            return render(request, 'register_user.html', context={'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginUserForm()
        return render(request, 'login.html', context={'form': form})

    def post(self, request):
        form = LoginUserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            username = data.get('username')
            password = data.get('password')

            user = User.objects.get(username=username, password=password)
            login(request, user)
            msg = f"zalogowano użytkownika {user}"
            return render(request, 'home.html', {'msg': msg})
        else:
            msg = 'bledne dane'
            return render(request, 'login.html', context={'form': form, 'msg': msg})


class LogoutView(View):
    def get(self, request):
        logout(request)
        msg = "wylogowano użytkownika"
        return render(request, 'home.html', {'msg': msg})


class AddCategory(View):
    def get(self, request):
        form = CategoryCreateForm()
        return render(request, 'add_category.html', context={'form': form})

    def post(self, request):
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BlogPostCategory.objects.create(name=data.get('name'), description=data.get('description'))
            return redirect('/')
        else:
            return render(request, 'add_category.html', context={'form': form})


class AddBlogPost(View):
    def get(self, request):
        form = BlogPostCreateForm()
        return render(request, 'add_blogpost.html', context={'form': form})

    def post(self, request):
        form = BlogPostCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            category_id = data.get('category')
            BlogPost.objects.create(title=data.get('title'), text=data.get('text'),
                                    category=BlogPostCategory.objects.get(id=category_id))
            return redirect('/')
        else:
            return render(request, 'add_blogpost.html', context={'form': form})


class AddArticleCategory(View):
    def get(self, request):
        form = ArticleCategoryCreateForm()
        return render(request, 'add_article_category.html', context={'form': form})

    def post(self, request):
        form = ArticleCategoryCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ArticleCategory.objects.create(name=data.get('name'), description=data.get('description'))
            return redirect('/')
        else:
            return render(request, 'add_article_category.html', context={'form': form})


class AddArticle(View):
    def get(self, request):
        form = ArticleCreateForm()
        return render(request, 'add_article.html', context={'form': form})

    def post(self, request):
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            category_id = data.get('category')
            Article.objects.create(title=data.get('title'), text=data.get('text'),
                                   category=BlogPostCategory.objects.get(id=category_id))
            return redirect('/')
        else:
            return render(request, 'add_article.html', context={'form': form})


class BlogPostView(View):
    def get(self, request, blogpost_id):
        blogpost = get_object_or_404(BlogPost, id=blogpost_id)
        category = BlogPostCategory.objects.get(id=blogpost.category_id)
        image = BlogPostImage.objects.get(blogpost_id=blogpost_id)
        context = {
            'image':image,
            'blogpost':blogpost,
            'category':category,
        }
        return render(request, 'blogpost.html', context)

class BlogAllPostsView(View):
    def get(self,request):
        blogposts=BlogPost.objects.all()
        category = BlogPostCategory.objects.all()
        images = BlogPostImage.objects.all()
        context = {
            'image': images,
            'blogpost': blogposts,
            'category': category,
        }
        return render(request, 'blog.html',context )

class BlogCategoryPosts(View):
    def get(self,request,category_id):
        blogposts=BlogPost.objects.filter(category_id=category_id)
        catname = BlogPostCategory.objects.get(id=category_id)
        images = BlogPostImage.objects.all()
        category=BlogPostCategory.objects.all()
        context = {
            'image': images,
            'blogpost': blogposts,
            'catname': catname,
            'category': category,
        }
        return render(request, 'blog.html', context)

class ArticleAllView(View):
    def get(self,request):
        articles=Article.objects.all()
        images=ArticleImage.objects.all()
        category=ArticleCategory.objects.all()
        context = {
            "articles":articles,
            "images":images,
            "category":category,
        }
        return render(request,'articles.html', context)

class ArticleView(View):
    def get(self,request,article_id):
        article = get_object_or_404(Article, id=article_id)
        category = ArticleCategory.objects.get(id=article.category_id)
        image = ArticleImage.objects.get(article_id=article_id)
        context = {
            "article": article,
            "image": image,
            "category": category,
        }
        return render(request, 'article.html', context)

class ArticleCategoryView(View):
    def get(self,request,category_id):
        articles=Article.objects.filter(category_id=category_id)
        catname=ArticleCategory.objects.get(id=category_id)
        images=Article.objects.all()
        category=ArticleCategory.objects.all()
        context = {
            'articles':articles,
            'images':images,
            'catname':catname,
            'category':category,
        }
        return render(request,'articles.html',context)

class QuizView(View):
    def get(self,request,category_id):
        request.session['score'] = 0
        all_ids=Question.objects.values_list("id",flat=True)
        random_ids=random.sample(list(all_ids),10)
        questions=Question.objects.filter(id__in=random_ids,category_id=category_id)
        return render(request, 'quiz.html',context={'questions':questions})

    def post(self,request,category_id):
        for i in range(1,11):
            question_id = request.POST.get(f"question_id_{i}")
            answer = request.POST.get(f"answer_{i}")
            question = Question.objects.get(id=question_id)
            if question.correct==answer:
                request.session['score']+=1

        if request.user.is_authenticated:
            score=request.session['score']
            Result.objects.create(amount=score,category_id=category_id,user_id=request.user.id)
            user_results =Result.objects.filter(user_id=request.user.id)
            y_points = []
            for results in user_results:y_points.append(results.amount)
            plt.title('Your results on plot')
            plt.ylabel('Points')
            plt.xlabel('attempts')
            plt.plot(y_points,marker='o')
            plt.ylim(1,11)
            plt.yticks(range(1,12), [str(i) if i<=10 else '' for i in range(1,12)])
            plt.xticks(range(len(y_points)), [str(i) for i in range(1,len(y_points)+1)])
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png=buffer.getvalue()
            buffer.close()
            graphic=base64.b64encode(image_png)
            graphic=graphic.decode('utf-8')

            users_results=Result.objects.all()
            hist_data=[]
            for results in users_results : hist_data.append(results.amount)
            plt.clf()
            plt.title('Users results')
            plt.ylabel('attempts')
            plt.xlabel('Points')
            plt.hist(hist_data)
            buffer=io.BytesIO()
            plt.savefig(buffer,format='png')
            buffer.seek(0)
            image_png=buffer.getvalue()
            buffer.close()
            graphic_hist=base64.b64encode(image_png)
            graphic_hist=graphic_hist.decode('utf-8')
            return render(request,'result.html',context={'score':score,"users_results":users_results, "plot":graphic, 'hist':graphic_hist})
        else:
            score = request.session['score']
            Result.objects.create(amount=score,category_id=category_id)

            users_results = Result.objects.all()
            hist_data = []
            for results in users_results: hist_data.append(results.amount)
            plt.clf()
            plt.title('Users results')
            plt.ylabel('attempts')
            plt.xlabel('Points')
            plt.hist(hist_data)
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            print("image_png:", image_png[:100])
            buffer.close()
            graphic_hist = base64.b64encode(image_png)
            print("graphic_hist:", graphic_hist[:100])
            graphic_hist = graphic_hist.decode('utf-8')
            return render(request,'result.html',context={'score':score,"users_results":users_results, 'hist':graphic_hist})

def questionview(request, question_id):
    q=Question.objects.get(id=question_id)
    return render(request,'questiontest.html',context={'q':q})
