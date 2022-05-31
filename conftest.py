import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_1(db):
    user = User.objects.create_user('unim')
    return user
