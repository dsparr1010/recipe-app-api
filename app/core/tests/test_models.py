from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email = 'test@gmail.com', password = 'some_pass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'test@gmail.com'
        password = 'some_pass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_new_user_email_normalized(self):
        """Test that the email for new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='some_pass'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test create new user without an email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'some_pass')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@gmail.com', 'some_pass')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user = sample_user(),
            name = 'Vegan'
        )

        self.assertEqual(str(tag), tag.name)
