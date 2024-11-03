from django.test import TestCase
from category.models import Category
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

class CategoryTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            category_name="Fiction",
            slug="fiction",
            category_image=SimpleUploadedFile("category_image.jpg", b"file_content", content_type="image/jpeg"), 
            category_des="A category for fictional books."
        )

    def test_create_category(self):
        self.assertEqual(self.category.category_name, "Fiction")
        self.assertEqual(self.category.slug, "fiction")
        self.assertTrue(self.category.category_image.url.startswith('/media/images/cat/'))
        self.assertEqual(self.category.category_des, "A category for fictional books.")

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), "Fiction")

    def test_unique_category_slug(self):
        with self.assertRaises(Exception):
            Category.objects.create(
                category_name="Another Fiction",
                slug="fiction",  
            )

    def test_update_category(self):
        self.category.category_name = "Updated Fiction"
        self.category.save()
        self.assertEqual(self.category.category_name, "Updated Fiction")

    def test_delete_category(self):
        category_id = self.category.id
        self.category.delete()
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=category_id)

    def test_category_description_max_length(self):
        long_description = 'B' * 2001  
        category = Category(
            category_name="Long Description Category",
            slug="long-description-category",
            category_des=long_description  
        )
        with self.assertRaises(ValidationError):
            category.full_clean()  

    def test_category_image_upload(self):
        new_category = Category.objects.create(
            category_name="Non-Fiction",
            slug="non-fiction",
            category_image=SimpleUploadedFile("non_fiction_image.jpg", b"file_content", content_type="image/jpeg"),
            category_des="A category for non-fictional books."
        )
        self.assertTrue(new_category.category_image.url.startswith('/media/images/cat/'))

    def test_create_category_with_blank_slug(self):
        with self.assertRaises(ValidationError):
            category = Category(
                category_name="Category with Blank Slug",
                slug="",  
                category_des="A category with a blank slug."
            )
            category.full_clean() 
            
    def test_category_retrieve_by_slug(self):
        category = Category.objects.get(slug="fiction")
        self.assertEqual(category, self.category)
            
    def test_category_unique_name(self):
        with self.assertRaises(Exception):
            Category.objects.create(
                category_name="Fiction",
                slug="new-fiction"
            )
   
    def test_category_update_description(self):
        self.category.category_des = "Updated description"
        self.category.save()
        self.assertEqual(Category.objects.get(slug="fiction").category_des, "Updated description")
