from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('layout/', views.main),
    path('o_nas/', views.about),
    path('services/', views.services),
    path('question/<int:question_id>', views.questionview),
    path('quiz/<int:category_id>', views.QuizView.as_view()),
    path('register/', views.RegisterUserView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('add_category/', views.AddCategory.as_view()),
    path('add_blogpost/', views.AddBlogPost.as_view()),
    path('add_article_category/', views.AddArticleCategory.as_view()),
    path('add_article/', views.AddArticle.as_view()),
    path('blog/', views.BlogAllPostsView.as_view()),
    path('blog/category/<int:category_id>', views.BlogCategoryPosts.as_view()),
    path('blogpost/<int:blogpost_id>',views.BlogPostView.as_view()),
    path('articles/',views.ArticleAllView.as_view()),
    path('article/<int:article_id>',views.ArticleView.as_view()),
    path('articles/category/<int:category_id>',views.ArticleCategoryView.as_view()),


]
