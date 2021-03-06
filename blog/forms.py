from django import forms
from django.forms import ModelForm
from .models import Article


class userCreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description', 'category', 'pub_date', 'image', 'status')
