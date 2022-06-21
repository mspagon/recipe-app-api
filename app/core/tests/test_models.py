"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with a successful email."""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            # ('input email', 'expected')
            ('test1@EXAMPLE.com', 'test1@example.com'),
            ('SOMEemail2@Example.com', 'SOMEemail2@example.com'),
            ('JOHN.DOE@ExAmPlE.cOM', 'JOHN.DOE@example.com'),
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email=email, password='sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='test123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

