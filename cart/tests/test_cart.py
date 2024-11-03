# cart/tests/test_cart.py
from django.test import TestCase, Client
from django.urls import reverse
from cart.models import Cart, CartItems
from bookstore.models import Book
from category.models import Category
from django.core.files.uploadedfile import SimpleUploadedFile

class CartTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(category_name="Fiction", slug="fiction")

        # Adding a mock image file to the book to avoid the 'image attribute has no file associated' error
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
        self.client.session.save()
        self.cart = Cart.objects.create(cart_session=self.client.session.session_key)

    def test_add_to_cart(self):
        response = self.client.get(reverse('add_cart', args=[self.book.slug]))
        self.assertEqual(response.status_code, 302)
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        self.assertTrue(CartItems.objects.filter(cart=cart, book=self.book).exists())

    def test_add_existing_book_to_cart(self):
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=1, is_active=True)
        self.client.get(reverse('add_cart', args=[self.book.slug]))

        item = CartItems.objects.get(cart=cart, book=self.book)
        self.assertEqual(item.quantity, 2)

    def test_cart_view(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html")

    def test_cart_total_price(self):
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=2, is_active=True)
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.context['total'], 40)

    def test_update_cart_item_quantity(self):
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=1, is_active=True)
        response = self.client.post(reverse('update_cart', args=[self.book.slug]), {'quantity': 3})
        item = CartItems.objects.get(cart=cart, book=self.book)
        self.assertEqual(item.quantity, 3)

    def test_delete_cart_item(self):
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=1, is_active=True)
        response = self.client.get(reverse('delete_cart_item', args=[self.book.slug]))
        self.assertFalse(CartItems.objects.filter(cart=cart, book=self.book).exists())

    def test_empty_cart(self):
        response = self.client.get(reverse('cart'))
        # Ensure the empty message is shown
        self.assertContains(response, 'Your cart is empty')

    def test_add_to_cart_without_session(self):
        self.client.session.flush()
        response = self.client.get(reverse('add_cart', args=[self.book.slug]))
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        self.assertTrue(cart)

    def test_update_cart_item_invalid_quantity(self):
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=1, is_active=True)
        response = self.client.post(reverse('update_cart', args=[self.book.slug]), {'quantity': -1})
        self.assertEqual(response.status_code, 302)  # Expect redirection or error handling

    def test_cart_items_count(self):
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=2, is_active=True)
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.context['cart_items'].count(), 1)

    def test_cart_item_status(self):
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        cart_item = CartItems.objects.create(cart=cart, book=self.book, quantity=1, is_active=True)
        self.assertTrue(cart_item.is_active)

    def test_add_to_cart_stock_update(self):
        self.client.get(reverse('add_cart', args=[self.book.slug]))
        self.book.refresh_from_db()
        self.assertEqual(self.book.stocks, 9)

    def test_cart_total_price_multiple_books(self):
        another_book = Book.objects.create(
            title="Another Book",
            slug="another-book",
            price=15,
            stocks=10,
            category=self.category,
            image=SimpleUploadedFile("another_book_image.jpg", b"file_content", content_type="image/jpeg")
        )
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=2, is_active=True)
        CartItems.objects.create(cart=cart, book=another_book, quantity=1, is_active=True)
        
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.context['total'], 55)  # 2*20 + 1*15

    def test_remove_item_from_cart_with_multiple_items(self):
        another_book = Book.objects.create(
            title="Another Book",
            slug="another-book",
            price=15,
            stocks=10,
            category=self.category,
            image=SimpleUploadedFile("another_book_image.jpg", b"file_content", content_type="image/jpeg")
        )
        
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=1, is_active=True)
        CartItems.objects.create(cart=cart, book=another_book, quantity=1, is_active=True)

        response = self.client.get(reverse('delete_cart_item', args=[self.book.slug]))
        self.assertFalse(CartItems.objects.filter(cart=cart, book=self.book).exists())
        self.assertTrue(CartItems.objects.filter(cart=cart, book=another_book).exists())  # Another book should still be there
    
    def test_update_non_existent_cart_item(self):
        response = self.client.post(reverse('update_cart', args=['non-existent-book-slug']), {'quantity': 1})
        self.assertEqual(response.status_code, 404)  # Expecting a not found error

    def test_cart_empty_after_deleting_all_items(self):
        another_book = Book.objects.create(
            title="Another Book",
            slug="another-book",
            price=15,
            stocks=10,
            category=self.category,
            image=SimpleUploadedFile("another_book_image.jpg", b"file_content", content_type="image/jpeg")
        )
        
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=1, is_active=True)
        CartItems.objects.create(cart=cart, book=another_book, quantity=1, is_active=True)

        self.client.get(reverse('delete_cart_item', args=[self.book.slug]))
        self.client.get(reverse('delete_cart_item', args=[another_book.slug]))

        response = self.client.get(reverse('cart'))
        self.assertContains(response, 'Your cart is empty')  # Ensure the empty message is shown

    def test_set_cart_item_quantity_below_one(self):
        cart = Cart.objects.get(cart_session=self.client.session.session_key)
        CartItems.objects.create(cart=cart, book=self.book, quantity=1, is_active=True)
        
        response = self.client.post(reverse('update_cart', args=[self.book.slug]), {'quantity': 0})  # Try setting quantity to zero
        item = CartItems.objects.get(cart=cart, book=self.book)
        self.assertEqual(item.quantity, 1)  # Quantity should not change
