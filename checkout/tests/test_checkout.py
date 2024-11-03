from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from checkout.models import order, order_list, invoice
from cart.models import Cart, CartItems
from bookstore.models import Book
from category.models import Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib import messages


User = get_user_model()


class CheckoutTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create data that is shared across all test methods
        cls.shared_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'address': '123 Street',
            'city': 'CityName',
            'division': 'Division',
            'zip': '12345',
            'country': 'CountryName',
            'transaction_id': '1234567890',
            'order_note': 'Please deliver quickly'
        }

    def setUp(self):
        #cliente
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='tuskact4',
            first_name='Test',
            last_name='User',
            phone='1234567890',
            email='testuser@example.com'
        )

        login_successful = self.client.login(email='testuser@example.com', password='tuskact4')
        self.assertTrue(login_successful, "User login failed")
        self.checkout_url = reverse('checkout_page')

        #crear datos
        self.data = self.shared_data.copy()  # Copy to avoid modification across tests


        self.category = Category.objects.create(category_name="Fiction", slug="fiction")
        self.book = Book.objects.create(
            title="Sample Book",
            slug="sample-book",
            price=20,
            stocks=10,
            category=self.category,
            image=SimpleUploadedFile("book_image.jpg", b"file_content", content_type="image/jpeg")  # Mock image file
        )
        # Create a cart for the session
        session = self.client.session
        session.create()
        self.cart = Cart.objects.create(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=self.cart, book=self.book, quantity=1, is_active=True)
        
        session.save()


    def test_checkout_page_loads(self):
        #Test that the checkout page loads successfully
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    def test_submit_checkout_form_valid(self):
        response = self.client.post(reverse('checkout_req'), self.data)
        self.assertEqual(response.status_code, 302)

    def test_submit_checkout_form_invalid_char(self):
        self.data['first_name'] = '#'
        response = self.client.post(reverse('checkout_req'), self.data, follow=True)
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertIn("Sorry, First Name can't contain a special character.", [str(message) for message in messages_list])

    def test_checkout_req_order_creation(self):
        #Test if an order is created upon successful checkout
        self.client.post(reverse('checkout_req'), self.data)
        self.assertTrue(invoice.objects.filter(transaction_id='1234567890').exists())

    def test_checkout_repeated_transaction_id_error(self):
        #Test invalid transaction ID error
        response1 = self.client.post(reverse('checkout_req'), self.data)
        response2 = self.client.post(reverse('checkout_req'), self.data, reverse=True)
        messages_list = list(messages.get_messages(response2.wsgi_request))
        self.assertIn("Sorry, transaction Id already exits.", [str(message) for message in messages_list])

    def test_checkout_without_login(self):
        #Test that unauthenticated users are redirected from checkout
        self.client.logout()
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/register', response.url)

    def test_checkout_minimal_information(self):
        #Test minimal valid information for checkout
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'address': '',
            'city': '',
            'division': '',
            'zip': '',
            'country': '',
            'transaction_id': '1234567890',
            'order_note': ''
        }
        self.client.post(reverse('checkout_req'), data)
        self.assertTrue(invoice.objects.filter(transaction_id='1234567890').exists())

    def test_checkout_invalid_division_code(self):
        #Test invalid zip code format
        self.data['division'] = '-1'
        response = self.client.post(reverse('checkout_req'), self.data, follow= True)
        self.assertTemplateUsed(response, 'checkout.html')  # Verifica que se usa la plantilla correcta
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertIn("Sorry, Division can't contain a number", [str(message) for message in messages_list])


    def test_checkout_form_data_persistence(self):
        #Test that form data persists correctly in the database
        data = {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'address': '456 Avenue',
            'city': 'AnotherCity',
            'division': 'SecondDivision',
            'zip': '54321',
            'country': 'CountryName',
            'transaction_id': '5555555555',
            'order_note' : 'Entrega rapida por favor'
        }
        self.client.post(reverse('checkout_req'), data)
        guardado = invoice.objects.get(transaction_id='5555555555')
        self.assertEqual(guardado.first_name, 'Alice')
        self.assertEqual(guardado.address, '456 Avenue')

    def test_checkout_page_security(self):
        #Test CSRF token presence in checkout form
        response = self.client.get(self.checkout_url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_checkout_redirect_after_success(self):
        #Test redirection to confirmation page after successful checkout
        response = self.client.post(reverse('checkout_req'), self.data)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/dashboard/orders', response.url)
