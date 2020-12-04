from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserTests(TestCase):

    def test_user_creation_form_for_creating_a_normal_user(self):
        user = User.objects.create_user(
            username="testuser",
            email="testuser@site.com",
            password="thepassword",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@site.com"),
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_user_creation_form_for_creating_a_superuser(self):
        user = User.objects.create_superuser(
            username="admin",
            email="admin@site.com",
            password="adminpassword"
        )
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@site.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)