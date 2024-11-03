from django.test import TestCase
from django.urls import reverse
from accounts.models import Account
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib import messages

# Testing the Account model
class AccountModelTests(TestCase):

    # 1
    def test_create_user(self):
        user = Account.objects.create_user(
            first_name='John',
            last_name='Doe',
            username='johndoe',
            email='john@example.com',
            phone='1234567890',
            password='password123'
        )
        self.assertEqual(user.username, 'johndoe')
        self.assertTrue(user.check_password('password123'))

    # 2
    def test_create_superuser(self):
        superuser = Account.objects.create_superuser(
            first_name='Admin',
            last_name='User',
            username='adminuser',
            email='admin@example.com',
            phone='0987654321',
            password='adminpassword'
        )
        self.assertEqual(superuser.username, 'adminuser')
        self.assertTrue(superuser.is_superuser)

    # 3
    def test_username_uniqueness(self):
        Account.objects.create_user(
            first_name='User1',
            last_name='Test1',
            username='uniqueuser',
            email='user1@example.com',
            phone='1112223333',
            password='password123'
        )
        with self.assertRaises(Exception):
            Account.objects.create_user(
                first_name='User2',
                last_name='Test2',
                username='uniqueuser',
                email='user2@example.com',
                phone='4445556666',
                password='password123'
            )

    # 4
    def test_email_uniqueness(self):
        Account.objects.create_user(
            first_name='User1',
            last_name='Test1',
            username='user1',
            email='unique@example.com',
            phone='1112223333',
            password='password123'
        )
        with self.assertRaises(Exception):
            Account.objects.create_user(
                first_name='User2',
                last_name='Test2',
                username='user2',
                email='unique@example.com',
                phone='4445556666',
                password='password123'
            )

    # 5
    def test_phone_uniqueness(self):
        Account.objects.create_user(
            first_name='User1',
            last_name='Test1',
            username='user1',
            email='user1@example.com',
            phone='9998887777',
            password='password123'
        )
        with self.assertRaises(Exception):
            Account.objects.create_user(
                first_name='User2',
                last_name='Test2',
                username='user2',
                email='user2@example.com',
                phone='9998887777',
                password='password123'
            )

    # 6
    def test_user_string_representation(self):
        user = Account.objects.create_user(
            first_name='Jane',
            last_name='Doe',
            username='janedoe',
            email='jane@example.com',
            phone='1234567890',
            password='password123'
        )
        self.assertEqual(str(user), 'jane@example.com')

    # 7
    def test_user_has_perm(self):
        user = Account.objects.create_user(
            first_name='John',
            last_name='Doe',
            username='johndoe',
            email='john@example.com',
            phone='1234567890',
            password='password123'
        )
        self.assertFalse(user.has_perm('some_permission'))

# Testing the views
class AccountViewTests(TestCase):

    # 8
    def test_registration_view_valid(self):
        response = self.client.post(reverse('register'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'password': 'password123',
            'confirm_password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertTrue(Account.objects.filter(username='johndoe').exists())

    # 9
    def test_registration_view_invalid_email(self):
        response = self.client.post(reverse('register'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'invalid-email',
            'phone': '1234567890',
            'password': 'password123',
            'confirm_password': 'password123',
        }, follow=True)
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertIn("Sorry, Email can't contain a special character.", [str(message) for message in messages_list])

    # 10
    def test_login_view_valid(self):
        Account.objects.create_user(
            first_name='John',
            last_name='Doe',
            username='johndoe',
            email='john@example.com',
            phone='1234567890',
            password='password123'
        )
        response = self.client.post(reverse('login'), {
            'email': 'john@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    # 11
    def test_login_view_invalid(self):
        response = self.client.post(reverse('login'), {
            'email': 'nonexistent@example.com',
            'password': 'wrongpassword'
        }, follow=True)
        self.assertEqual(response.status_code, 200)  # Renders login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    # 12
    def test_logout_view(self):
        self.client.login(email='john@example.com', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirects after logout
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    # 13
    def test_profile_edit_view_valid(self):
        user = Account.objects.create_user(
            first_name='John',
            last_name='Doe',
            username='johndoe',
            email='john@example.com',
            phone='1234567890',
            password='password123'
        )
        self.client.login(email='john@example.com', password='password123')
        response = self.client.post(reverse('profile_edit'), {
            'first_name': 'John',
            'last_name': 'Compiler',
            'email': 'john@example.com',
            'phone': '1234567890',
        }, follow= True)
        user2 = Account.objects.get(email='john@example.com')
        self.assertEqual(user2.last_name, 'Compiler')
"""
    # 14
    def test_profile_edit_view_invalid_email(self):
        self.client.login(email='john@example.com', password='password123')
        response = self.client.post(reverse('profile_edit'), {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'invalid-email',
            'phone': '1234567890',
        })
        self.assertEqual(response.status_code, 200)  # Renders edit profile page
        self.assertFormError(response, 'form', 'email', "Enter a valid email address.")

    # 15
    def test_change_password_view_valid(self):
        user = Account.objects.create_user(
            first_name='Jane',
            last_name='Doe',
            username='janedoe',
            email='jane@example.com',
            phone='0987654321',
            password='password123'
        )
        self.client.login(email='jane@example.com', password='password123')
        response = self.client.post(reverse('change_pwd'), {
            'old_password': 'password123',
            'password': 'newpassword456',
            'verify_password': 'newpassword456',
        })
        self.assertEqual(response.status_code, 302)  # Redirects on success
        user.refresh_from_db()
        self.assertTrue(user.check_password('newpassword456'))

    # 16
    def test_change_password_view_incorrect_old_password(self):
        user = Account.objects.create_user(
            first_name='Jane',
            last_name='Doe',
            username='janedoe',
            email='jane@example.com',
            phone='0987654321',
            password='password123'
        )
        self.client.login(email='jane@example.com', password='password123')
        response = self.client.post(reverse('change_pwd'), {
            'old_password': 'wrongpassword',
            'password': 'newpassword456',
            'verify_password': 'newpassword456',
        })
        self.assertEqual(response.status_code, 200)  # Renders change password page
        self.assertFormError(response, 'form', 'old_password', "Sorry, your old password doesn't match our record.")

    # 17
    def test_change_password_view_non_matching(self):
        user = Account.objects.create_user(
            first_name='Jane',
            last_name='Doe',
            username='janedoe',
            email='jane@example.com',
            phone='0987654321',
            password='password123'
        )
        self.client.login(email='jane@example.com', password='password123')
        response = self.client.post(reverse('change_pwd'), {
            'old_password': 'password123',
            'password': 'newpassword456',
            'verify_password': 'differentpassword',
        })
        self.assertEqual(response.status_code, 200)  # Renders change password page
        self.assertFormError(response, 'form', 'verify_password', "The two password fields didn't match.")

    # 18
    def test_inactive_user_login(self):
        user = Account.objects.create_user(
            first_name='John',
            last_name='Doe',
            username='johndoe',
            email='john@example.com',
            phone='1234567890',
            password='password123'
        )
        user.is_active = False
        user.save()
        response = self.client.post(reverse('login'), {
            'email': 'john@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)  # Renders login page
        self.assertContains(response, "Your account has been disabled.")

    # 19
    def test_password_reset_request_view(self):
        response = self.client.post(reverse('password_reset'), {
            'email': 'nonexistent@example.com'
        })
        self.assertEqual(response.status_code, 200)  # Renders password reset page
        self.assertContains(response, "We have emailed you a link to reset your password.")

    # 20
    def test_password_reset_with_valid_user(self):
        user = Account.objects.create_user(
            first_name='Alice',
            last_name='Doe',
            username='alicedoe',
            email='alice@example.com',
            phone='1234567890',
            password='password123'
        )
        response = self.client.post(reverse('dashboard/change_pwd'), {
            'email': 'alice@example.com'
        })
        self.assertEqual(response.status_code, 200)  # Renders password reset page
        self.assertContains(response, "We have emailed you a link to reset your password.")

    # 21
    def test_profile_view_for_logged_in_user(self):
        user = Account.objects.create_user(
            first_name='Charlie',
            last_name='Brown',
            username='charlie',
            email='charlie@example.com',
            phone='1234567890',
            password='password123'
        )
        self.client.login(email='charlie@example.com', password='password123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Charlie Brown')

    # 22
    def test_profile_view_for_non_logged_in_user(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirects to login

    # 23
    def test_account_deactivation(self):
        user = Account.objects.create_user(
            first_name='David',
            last_name='Smith',
            username='david',
            email='david@example.com',
            phone='1234567890',
            password='password123'
        )
        self.client.login(email='david@example.com', password='password123')
        response = self.client.post(reverse('deactivate_account'))
        self.assertEqual(response.status_code, 302)  # Redirects after deactivation
        self.assertFalse(Account.objects.filter(email='david@example.com').exists())

    # 24
    def test_password_reset_confirmation_valid_token(self):
        user = Account.objects.create_user(
            first_name='Emma',
            last_name='Johnson',
            username='emma',
            email='emma@example.com',
            phone='1234567890',
            password='password123'
        )
        # Assume we have a method to generate token, normally done by Django itself
        token = 'dummy-token'  # This should be replaced with a valid token generation
        response = self.client.post(reverse('password_reset_confirm', args=[token]), {
            'new_password': 'newpassword456',
            'confirm_password': 'newpassword456'
        })
        self.assertEqual(response.status_code, 302)  # Redirects on success
        user.refresh_from_db()
        self.assertTrue(user.check_password('newpassword456'))

    # 25
    def test_password_reset_confirmation_invalid_token(self):
        response = self.client.post(reverse('password_reset_confirm', args=['invalid-token']), {
            'new_password': 'newpassword456',
            'confirm_password': 'newpassword456'
        })
        self.assertEqual(response.status_code, 200)  # Renders confirmation page
        self.assertContains(response, "The password reset link is invalid.")
"""