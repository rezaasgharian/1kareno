from django.test import TestCase
from django.urls import reverse, resolve
from .views import *
from selenium import webdriver

# Create your tests here.


browser = webdriver.chrome()
browser.get('http://localhost:8000/blog')
browser.find_element_by_xpath('//*[@id="nav"]/li[5]/a').click()


#
# class FunctionalTestCase(TestCase):
#     # def test_blog_page(self):
#         pass
#
# class UnitTestCase(TestCase):
#     pass
#
# class UrlsTests(TestCase):
#     def test_fibonacci_url_is_resolved(self):
#         url = reverse('index')
#         self.assertEquals(resolve(url).func, index)


