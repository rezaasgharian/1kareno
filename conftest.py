import pytest
from django.contrib.auth.models import User
from blog.models import Article


@pytest.fixture
def new_user_factory(db):
    def create_user(
            username: str = 'username',
            password: str = None,
            first_name: str = 'firstname',
            last_name: str = 'lastname',
            email: str = 'test@gmail.com',
            is_staff: str = False,
            is_superuser: str = False,
            is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_user


@pytest.fixture()
def new_user(db, new_user_factory):
    return new_user_factory('uniman', '1216', 'Reza')


# @pytest.fixture()
# def user_1(db):
#     user1 = User.objects.create_user('Reza', 'reza@gmil.com')
#     return user1


@pytest.fixture()
def article_1(db):
    return Article.objects.create(title='Django', user_id=20)
