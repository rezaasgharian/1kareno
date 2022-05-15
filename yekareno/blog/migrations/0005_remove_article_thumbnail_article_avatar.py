# Generated by Django 4.0.3 on 2022-05-11 20:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='article',
            name='avatar',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/avatars'),
            preserve_default=False,
        ),
    ]
