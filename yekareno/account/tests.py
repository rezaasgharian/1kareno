from django.test import TestCase
from .models import Profile


# Create your tests here.
class TestUrl(TestCase):
    def testProfilePage(self):
        response = self.client.get('')
        print(response)
        self.assertEqual(response.status_code, 200)


class TestModel(TestCase):
    def testProfileModel(self):
        phone = Profile.objects.create(phone='09128503061')
        self.assertIs(str(phone), '09128503061')