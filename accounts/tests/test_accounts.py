from django.test import TestCase
from django.urls import reverse
from accounts.models import Account
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError

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

    # 8
    def test_user_is_active_default(self):
        user = Account.objects.create_user(
            first_name='Active',
            last_name='User',
            username='activeuser',
            email='active@example.com',
            phone='1234567890',
            password='password123'
        )
        self.assertTrue(user.is_active)

    # 9
    def test_superuser_is_admin(self):
        superuser = Account.objects.create_superuser(
            first_name='Admin',
            last_name='User',
            username='superadmin',
            email='admin@example.com',
            phone='0987654321',
            password='adminpassword'
        )
        self.assertTrue(superuser.is_admin)

    # 10
    def test_user_repr(self):
        user = Account.objects.create_user(
            first_name='Jane',
            last_name='Smith',
            username='janesmith',
            email='jane.smith@example.com',
            phone='1234567890',
            password='password123'
        )
        self.assertEqual(str(user), 'jane.smith@example.com')

    # 11
    def test_superuser_permissions(self):
        superuser = Account.objects.create_superuser(
            first_name='Super',
            last_name='User',
            username='superuser',
            email='superuser@example.com',
            phone='9876543210',
            password='superpassword'
        )
        self.assertTrue(superuser.has_perm('some_permission'))

    # 12
    def test_user_has_no_perm(self):
        user = Account.objects.create_user(
            first_name='Regular',
            last_name='User',
            username='regularuser',
            email='regular@example.com',
            phone='1234567890',
            password='password123'
        )
        self.assertFalse(user.has_perm('some_permission'))

    # 13
    def test_email_field_max_length(self):
        user = Account.objects.create_user(
            first_name='Long',
            last_name='Email',
            username='longemailuser',
            email='longemailuser@example.com',
            phone='1234567890',
            password='password123'
        )
        self.assertEqual(len(user.email), 25)  # Longitud máx?

    # 21
    def test_username_max_length(self):
        long_username = 'u' * 101  # 101 de longitud
        with self.assertRaises(ValidationError):
            user = Account.objects.create_user(
                first_name='User',
                last_name='Test',
                username=long_username,
                email='test@example.com',
                phone='1234567890',
                password='password123'
            )
            user.full_clean()  #Lanza la validación

    # 25
    def test_user_creation_sets_fields_correctly(self):
        user = Account.objects.create_user(
            first_name='Alice',
            last_name='Wonderland',
            username='alicewonder',
            email='alice@example.com',
            phone='1234567890',
            password='alicepassword'
        )
        
        # Campos establecidos correctamente
        self.assertEqual(user.first_name, 'Alice')
        self.assertEqual(user.last_name, 'Wonderland')
        self.assertEqual(user.username, 'alicewonder')
        self.assertEqual(user.email, 'alice@example.com')
        self.assertEqual(user.phone, '1234567890')
        
        # Usuario está activo por defecto
        self.assertTrue(user.is_active)
        
        # Usuario no es un superusuario
        self.assertFalse(user.is_superuser)
        
        # Contraseña establecida correctamente
        self.assertTrue(user.check_password('alicepassword'))

    # 26
    def test_superuser_creation_sets_fields_correctly(self):
        superuser = Account.objects.create_superuser(
            first_name='Bob',
            last_name='Builder',
            username='bobthebuilder',
            email='bob@example.com',
            phone='9876543210',
            password='bobpassword'
        )

        # Campos establecidos correctamente
        self.assertEqual(superuser.first_name, 'Bob')
        self.assertEqual(superuser.last_name, 'Builder')
        self.assertEqual(superuser.username, 'bobthebuilder')
        self.assertEqual(superuser.email, 'bob@example.com')
        self.assertEqual(superuser.phone, '9876543210')
        
        #Superusuario tiene permisos correctos
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_admin)
        
        # Contraseña establecida correctamente
        self.assertTrue(superuser.check_password('bobpassword'))

# Testing the views
class AccountViewTests(TestCase):

    # 14
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

    # 15
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

    # 16
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

    # 17
    def test_login_view_invalid(self):
        response = self.client.post(reverse('login'), {
            'email': 'nonexistent@example.com',
            'password': 'wrongpassword'
        }, follow=True)
        self.assertEqual(response.status_code, 200)  # Renders login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    # 18
    def test_logout_view(self):
        self.client.login(email='john@example.com', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirects after logout
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    # 19
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

    # 20
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

    # 22
    def test_login_view_no_user(self):
        response = self.client.post(reverse('login'), {
            'email': 'nonexistent@example.com',
            'password': 'password123'
        }, follow=True)
        self.assertEqual(response.status_code, 200)  # Renders login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertIn("Sorry your Email/Password don't match", [str(message) for message in messages_list])

    # 23
    def test_change_password_view_mismatched_passwords(self):
        user = Account.objects.create_user(
            first_name='Bob',
            last_name='Brown',
            username='bobbrown',
            email='bob@example.com',
            phone='1234567890',
            password='password123'
        )
        self.client.login(email='bob@example.com', password='password123')
        response = self.client.post(reverse('change_pwd'), {
            'old_password': 'password123',
            'password': 'newpassword456',
            'verify_password': 'mismatchedpassword',  # Different from 'newpassword456'
        }, follow=True)
        self.assertEqual(response.status_code, 200)  # Stay on the change password page
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertIn("Sorry your password and verify password doesn't match.", [str(message) for message in messages_list])

    # 24
    def test_profile_view_redirects_if_not_authenticated(self):
        response = self.client.get(reverse('profile_edit'))
        self.assertEqual(response.status_code, 302)  # Redirige al inicio de sesión
        self.assertRedirects(response, '/login?next=/dashboard/profile_edit')  # Verifica la redirección al inicio de sesión
