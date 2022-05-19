from django.test import TestCase
from django.test import Client
from django.urls import reverse

client = Client()

class DictTestCase(TestCase):
    def test_no_explain(self):
        # pass
        res = self.client.get(reverse("word:explain", args=["hello"]))
        self.assertEqual(res.status_code, 200)
