from django.test import TestCase, Client
from bookstore.models import Book
from category.models import Category
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

class BookstoreTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            category_name="Fiction",
            slug="fiction"
        )

       
        self.book = Book.objects.create(
            title="Sample Book",
            slug="sample-book",
            price=20,
            stocks=10,
            category=self.category,
            image=SimpleUploadedFile("book_image.jpg", b"file_content", content_type="image/jpeg")  # Mock image file
        )

    def test_create_book(self):
        self.assertEqual(self.book.title, "Sample Book")
        self.assertEqual(self.book.price, 20)
        self.assertEqual(self.book.stocks, 10)

    def test_read_book(self):
        book = Book.objects.get(slug="sample-book")
        self.assertEqual(book.title, "Sample Book")

    def test_update_book(self):
        self.book.title = "Updated Sample Book"
        self.book.save()
        self.assertEqual(self.book.title, "Updated Sample Book")

    def test_delete_book(self):
        book_id = self.book.id
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)

    def test_unique_book_slug(self):
        with self.assertRaises(Exception):
            Book.objects.create(
                title="Another Sample Book",
                slug="sample-book",  
                price=25,
                stocks=5,
                category=self.category
            )


    def test_book_string_representation(self):
        self.assertEqual(str(self.book), "Sample Book")

    def test_book_description_max_length(self):
        long_description = 'A' * 3001  
        book = Book(
            title="Long Description Book",
            slug="long-description-book",
            category=self.category,
            price=15,
            stocks=5,
            description=long_description  
        )
        
        with self.assertRaises(ValidationError):
            book.full_clean()  

    def test_update_book_stock(self):
        self.book.stocks += 5
        self.book.save()
        self.assertEqual(self.book.stocks, 15)

    def test_add_book_with_image(self):
        new_book = Book.objects.create(
            title="Another Book",
            slug="another-book",
            price=15,
            stocks=5,
            category=self.category,
            image=SimpleUploadedFile("another_book_image.jpg", b"file_content", content_type="image/jpeg")
        )
        self.assertTrue(new_book.image.url.startswith('/media/images/books_img/'))

    def test_create_book_with_blank_fields(self):
        book = Book(
            title="Book with Blank Fields",
            slug="book-with-blank-fields",
            price=25,
            stocks=5,
            category=self.category,
            image=SimpleUploadedFile("blank_fields_book_image.jpg", b"file_content", content_type="image/jpeg"),
            author="",  
            description=""  
        )
        book.full_clean() 
        book.save()
        self.assertTrue(Book.objects.filter(title="Book with Blank Fields").exists())
        
    def test_create_book_with_invalid_price(self):
        with self.assertRaises(ValidationError):
            book = Book(
                title="Invalid Price Book",
                slug="invalid-price-book",
                price=-10,  
                stocks=5,
                category=self.category,
            )
            book.full_clean()  

    def test_create_book_with_negative_stocks(self):
        with self.assertRaises(ValidationError):
            book = Book(
                title="Invalid Stocks Book",
                slug="invalid-stocks-book",
                price=15,
                stocks=-5,  
                category=self.category,
            )
            book.full_clean()  

    def test_create_book_with_slug_collision(self):
        Book.objects.create(
            title="Another Book",
            slug="unique-slug", 
            price=30,
            stocks=10,
            category=self.category,
        )
        
        with self.assertRaises(ValidationError):
            book = Book(
                title="Collision Book",
                slug="unique-slug",  
                price=25,
                stocks=5,
                category=self.category,
            )
            book.full_clean() 

    
    def test_retrieve_book(self):
        retrieved_book = Book.objects.get(slug=self.book.slug)
        self.assertEqual(retrieved_book.title, self.book.title)
        self.assertEqual(retrieved_book.price, self.book.price)
        self.assertEqual(retrieved_book.stocks, self.book.stocks)
        self.assertEqual(retrieved_book.category, self.book.category)
    
    def test_book_price_validation(self):
        with self.assertRaises(ValidationError):
            invalid_book = Book(
                title="Invalid Price Book",
                slug="invalid-price-book",
                price=-10,  
                stocks=5,
                category=self.category,
            )
            invalid_book.full_clean()  
