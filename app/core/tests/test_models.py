"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user where the email and password are successful"""
        email = 'test@example.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            username=email,
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)
