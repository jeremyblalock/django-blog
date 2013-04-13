from django.test import TestCase
from models import *
from markdown import markdown


class PostTests(TestCase):
    def setUp(self):
        self.p1_title = 'Hello, world'
        self.p1_body = '# Title\n\nbody\n\n* Item 1\n* Item 2\n* Item 3\n'
        self.post1 = Post(title=self.p1_title,
                          body_md=self.p1_body,
                          author=None)
        self.post1.save()
    def test_save(self):
        expected = markdown(self.p1_body)
        self.assertEqual(self.post1.body, markdown(self.p1_body))

