from django.test import TestCase
from .models import User

# Create your tests here.
class UserTestCase(TestCase):

    user = User()

    def setUp(self):
        self.user = User.objects.create(name="joe",email="joe@mail.com")

    def test_user_is_registered(self):
        self.assertIs(User.is_registered(self.user.email),True)
