import pytest

class TestOne():
    def test_1(self):
       assert 1 == 1

    # @pytest.mark.uniman
    def test_2(self):
        assert 'a' in 'rezoo'

    def test_3(self):
        assert 5*5 == 25

@pytest.fixture()
def fixture_1():
    return 1

def test_fixture_1(fixture_1):
    num = fixture_1
    assert 1 == num


