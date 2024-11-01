# cart/tests/test_cart.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from cart.models import Cart, CartItems
from bookstore.models import Book

User = get_user_model()

class CartTests(TestCase):
    def setUp(self):
        # Set up user and session for the tests
        self.client = Client()
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="password123"
        )
        self.book = Book.objects.create(
            title="Test Book",
            slug="test-book",
            price=10,
            stocks=100,
            stocks_available=True
        )
        self.cart_url = reverse("cart")

    def test_add_item_to_cart(self):
        # Add an item to the cart
        self.client.login(email="testuser@example.com", password="password123")
        response = self.client.get(reverse("add_cart", args=[self.book.slug]))
        self.assertEqual(response.status_code, 302)
        cart_item = CartItems.objects.get(book=self.book)
        self.assertEqual(cart_item.quantity, 1)

    def test_increase_quantity_of_existing_cart_item(self):
        # Add item, then add again to increase quantity
        self.client.login(email="testuser@example.com", password="password123")
        self.client.get(reverse("add_cart", args=[self.book.slug]))
        self.client.get(reverse("add_cart", args=[self.book.slug]))
        cart_item = CartItems.objects.get(book=self.book)
        self.assertEqual(cart_item.quantity, 2)

    def test_update_cart_item_quantity(self):
        # Add item and update quantity
        self.client.login(email="testuser@example.com", password="password123")
        self.client.get(reverse("add_cart", args=[self.book.slug]))
        response = self.client.post(reverse("update_cart"), {
            "book_slug": self.book.slug,
            "quantity": 3
        })
        self.assertEqual(response.status_code, 302)
        cart_item = CartItems.objects.get(book=self.book)
        self.assertEqual(cart_item.quantity, 3)

    def test_delete_cart_item(self):
        # Add item, then delete it
        self.client.login(email="testuser@example.com", password="password123")
        self.client.get(reverse("add_cart", args=[self.book.slug]))
        response = self.client.get(reverse("delete_cart_item", args=[self.book.slug]))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(CartItems.DoesNotExist):
            CartItems.objects.get(book=self.book)

    def test_view_cart_contents(self):
        # Add multiple items to cart and check cart contents
        self.client.login(email="testuser@example.com", password="password123")
        self.client.get(reverse("add_cart", args=[self.book.slug]))
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_add_item_to_cart_without_session(self):
        # Add item without session key; session should be created
        response = self.client.get(reverse("add_cart", args=[self.book.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cart.objects.filter(cart_session=self.client.session.session_key).exists())

    def test_cart_total_calculation(self):
        # Add items and verify total calculation
        self.client.login(email="testuser@example.com", password="password123")
        self.client.get(reverse("add_cart", args=[self.book.slug]))
        self.client.get(reverse("add_cart", args=[self.book.slug]))
        response = self.client.get(self.cart_url)
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        cart_items = CartItems.objects.filter(cart=cart)
        total = sum(item.book.price * item.quantity for item in cart_items)
        self.assertContains(response, total)

    def test_cart_initialization_on_session_creation(self):
        # Ensure a cart is created with a new session
        self.client.get(self.cart_url)
        self.assertTrue(Cart.objects.filter(cart_session=self.client.session.session_key).exists())

    def test_add_inactive_cart_item(self):
        # Add inactive item, verify it doesn't appear in cart
        cart = Cart.objects.create(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=1, is_active=False)
        response = self.client.get(self.cart_url)
        self.assertNotContains(response, self.book.title)

    def test_cart_total_with_different_quantities(self):
        # Add items with varying quantities and check total
        self.client.login(email="testuser@example.com", password="password123")
        self.client.get(reverse("add_cart", args=[self.book.slug]))
        self.client.post(reverse("update_cart"), {"book_slug": self.book.slug, "quantity": 5})
        response = self.client.get(self.cart_url)
        expected_total = self.book.price * 5
        self.assertContains(response, expected_total)
