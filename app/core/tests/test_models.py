from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_email_successfull(self):
        """ Test creating a new user with an email is successfull"""
        email = "test@londonappdev.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(email = email, password=password)

        self.assertEqual(user.email , email)
        self.assertTrue(user.check_password(password))


    def test_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = "test@LONDONAPPDEV.com"
        user = get_user_model().objects.create_user(
            email = email,
            password = 'Test123!',

        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_envalid_email(self):
        """Test creating new user with no error rising error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password="Test123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(email='test@londondev.com',password = "Test123!")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_stuff)
