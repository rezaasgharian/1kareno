from django.urls import path
from .views import index, products, articles, articleDetail, create_article, base

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('products', products, name='products'),
    path('articles', articles, name='articles'),
    # path('profile/', profile, name='profile'),
    path('articleDetail/<int:id>', articleDetail, name='articleDetail'),
    path('create-article', create_article, name='createArticle'),
    path('base', base, name='base'),
]