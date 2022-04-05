from django.urls import path
from .views import index, products, articles, articleDetail

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('products', products, name='products'),
    path('articles', articles, name='articles'),
    path('articleDetail/<int:id>', articleDetail, name='articleDetail'),
]