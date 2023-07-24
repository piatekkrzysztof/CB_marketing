from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import *


def main(request):
    return render(request, 'layout.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


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