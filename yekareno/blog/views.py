from django.shortcuts import render
from .models import Product, Category, Article
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def category(request):
    categories = Category.objects.all()

def products(request):
    products = Product.objects.all()
    return render(request, 'blog/products.html', {'products': products})

def articles(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles.html', {'articles': articles})

def articleDetail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/articleDetail.html', {'articleDetail': article})

def base(request):
    return render(request, 'base.html')