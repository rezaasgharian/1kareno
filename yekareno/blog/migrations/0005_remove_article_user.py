# Generated by Django 4.0.3 on 2022-04-16 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_status_article_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
    ]
