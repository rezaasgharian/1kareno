from django.shortcuts import render, redirect
from .models import Product, Category, Article
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def category(request):
    categories = Category.objects.all()
    return render(request, 'blog/create_article.html', {'category': categories})


def products(request):
    products = Product.objects.all()
    return render(request, 'blog/products.html', {'products': products})


@login_required
def articles(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles.html', {'articles': articles})


@login_required
def create_article(request):
    if request.method == 'POST':
        form = userCreateArticle(request.POST)
        print(form)
        # if form.is_valid():
        #     data = form.cleaned_data
        #     print(request)
        #     Article.objects.create(user_id=request.user.id, title=data['title'], description=data['description'],
        #                            category=data['category'], pub_date=data['pub_date'],
        #                            status=data['status'], image=data['image'])
        #     # return redirect('blog:articles')
        #     return HttpResponse('Your article is added')
        # else:
        #     print(form.data)
        #     print(form.errors)
    else:
        categories = Category.objects.all()
        user_article = userCreateArticle()
        return render(request, 'blog/create_article.html', {'user_article': user_article, 'categories': categories})


@login_required
def articleDetail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/articleDetail.html', {'articleDetail': article})


def base(request):
    return render(request, 'base.html')
