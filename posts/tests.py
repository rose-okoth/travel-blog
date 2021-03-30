from django.test import TestCase
from .models import Post
import datetime as dt
from django.contrib.auth.models import User

class UserTestClass(TestCase):

# Set up method
    def setUp(self):
        self.rose= User(username = 'Rose', password = '123456789')

# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rose,User))

class PostTestClass(TestCase):
    
    def setUp(self):
        # Creating a new user and saving it
        self.rose= user(first_name = 'Rose', last_name ='Okoth', email ='okoth.rose@gmail.com')
        self.rose.save_user()

        # Creating a new tag and saving it
        self.new_slug = slug(name = 'testing')
        self.new_slug.save()
        self.new_post= Post(title = 'Test Post',content = 'This is a random test',editor = self.rose)
        self.new_post.save()
        self.new_post.slug.add(self.new_slug)

        def tearDown(self):
            User.objects.all().delete()
            Post.objects.all().delete()

    