from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@medellin.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )  # noqa
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Text the email for the new user is normalized"""
        email = "test@MEDELLIN.COM"

        user = get_user_model().objects.create_user(email, "test123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@medellin.com", "test123"
        )  # noqa

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
