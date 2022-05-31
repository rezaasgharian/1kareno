import pytest
from django.contrib.auth.models import User
from blog.models import *


@pytest.fixture()
def user_1(db):
    return User.objects.create_user('Reza')

@pytest.mark.django_db
def test_check_password(user_1):
    user_1.set_password('1216')
    assert user_1.check_password('1216') is True


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
