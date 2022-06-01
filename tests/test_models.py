import pytest
from django.contrib.auth.models import User
from blog.models import *


# def test_check_password(user_1):
#     user_1.set_password('1216')
#     print(user_1.password)
#     assert user_1.check_password('1216') is True
#
#
# def test_check_email(user_1):
#     print(user_1.email)
#     assert user_1.email == 'reza@gmil.com'
#
#
# def test_username(user_1):
#     assert user_1.username == 'Reza'


def test_new_user(new_user):
    assert new_user.username == 'uniman'


# def test_create_article(article_1):
#     assert article_1.title == 'Django'

# @pytest.mark.django_db
# def test_create_user():
#     User.objects.create_user('Unim', 'reza@gmail.com', 'ali')
#     count = User.objects.all().count()
#     assert count == 1
#
#
# @pytest.mark.django_db
# def test_create_article():
#     Product.objects.create()
#     count = Product.objects.all().count()
#     print(count)
#     assert count == 1


#
# def test_create_article():
#     title = Category.objects.get(title = 'HEY....!')
#     assert 1 == 1
#
