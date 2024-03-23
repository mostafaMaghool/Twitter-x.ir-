from django.test import TestCase
from . models import post
# Create your tests here.

class PostModelTest(TestCase):
    def setup(self):
        post.objects.create(text = "just a test")

    def test_text_cotent(self):
        Post = post.objects.get(id=1)
        excepted_object_name = f'{Post.text}'
        self.assertEqual(excepted_object_name, "just a test")