# boihut/category/tests/test_category.py

from django.test import TestCase
from category.models import Category
from django.core.exceptions import ValidationError

class CategoryModelTests(TestCase):
    
    def setUp(self):
        # Set up two sample categories
        self.category1 = Category.objects.create(
            category_name="Fiction",
            slug="fiction",
            category_des="Category for fiction books"
        )
        self.category2 = Category.objects.create(
            category_name="Non-Fiction",
            slug="non-fiction",
            category_des="Category for non-fiction books"
        )

    def test_category_creation(self):
        """Test if a category is created successfully"""
        self.assertEqual(self.category1.category_name, "Fiction")
        self.assertEqual(self.category1.slug, "fiction")
    
    def test_category_str_method(self):
        """Test the __str__ method of Category model"""
        self.assertEqual(str(self.category1), "Fiction")
    
    def test_category_slug_unique(self):
        """Test that the slug field is unique"""
        with self.assertRaises(Exception):
            Category.objects.create(
                category_name="Fiction",
                slug="fiction"
            )

    def test_category_name_max_length(self):
        """Test that category_name cannot exceed 100 characters"""
        long_name = "a" * 101
        category = Category(category_name=long_name, slug="long-name-slug")
        with self.assertRaises(ValidationError):
            category.full_clean()  # This will raise ValidationError if the max_length is exceeded


    def test_category_slug_max_length(self):
        """Test that slug cannot exceed 20 characters"""
        long_slug = "a" * 21
        category = Category(category_name="Test Category", slug=long_slug)
        with self.assertRaises(ValidationError):
            category.full_clean()

    def test_category_image_blank_allowed(self):
        """Test if category_image can be blank"""
        category = Category.objects.create(
            category_name="Science",
            slug="science"
        )
        self.assertEqual(category.category_image.name, "")

    def test_category_description_optional(self):
        """Test if category description can be blank"""
        category = Category.objects.create(
            category_name="History",
            slug="history"
        )
        self.assertEqual(category.category_des, "")

    def test_category_unique_name(self):
        """Test that the category_name is unique"""
        with self.assertRaises(Exception):
            Category.objects.create(
                category_name="Fiction",
                slug="new-fiction"
            )

    def test_category_retrieve_by_slug(self):
        """Test retrieving a category by its slug"""
        category = Category.objects.get(slug="fiction")
        self.assertEqual(category, self.category1)

    def test_category_update_description(self):
        """Test updating the description of a category"""
        self.category1.category_des = "Updated description"
        self.category1.save()
        self.assertEqual(Category.objects.get(slug="fiction").category_des, "Updated description")
