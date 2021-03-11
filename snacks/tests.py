from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Snacks

class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email='tester@email.com', password="pass"
        )

        self.snack = Snacks.objects.create(
            name="test", description="description test", owner=self.user,
        )

        
