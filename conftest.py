import pytest
from django.contrib.auth.models import User
from blog.models import Article


# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user('unim')
#     return user

@pytest.fixture()
def user_1(db):
    return User.objects.create_user('Reza', 'reza@gmil.com')


@pytest.fixture()
def article_1(db):
    return Article.objects.create(title='Django', user_id=20)
