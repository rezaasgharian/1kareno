from django.test import TestCase
from django.urls import reverse, resolve
from .views import *

# Create your tests here.


class UrlsTests(TestCase):
    def test_fibonacci_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

