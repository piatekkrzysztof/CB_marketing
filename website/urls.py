from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('layout/', views.main),
    path('o_nas/', views.about),
    path('register/', views.RegisterUserView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('add_category/', views.AddCategory.as_view()),
    path('add_blogpost/', views.AddBlogPost.as_view()),
    path('add_article_category/', views.AddArticleCategory.as_view()),
    path('add_article/', views.AddArticle.as_view()),
    path('blog/', views.BlogAllPostsView.as_view()),
    path('blogpost/<int:blogpost_id>',views.BlogPostView.as_view()),
]
