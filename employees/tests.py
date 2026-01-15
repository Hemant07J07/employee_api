# employees/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Employee

class EmployeeAPITest(APITestCase):
    def setUp(self):
        # create a test user and force-authenticate (avoids JWT token handling in unit tests)
        self.user = User.objects.create_user(username="tester", password="testpass123")
        self.client.force_authenticate(user=self.user)

    def test_create_employee(self):
        url = reverse("employee-list")
        data = {"name": "Bob", "email": "bob@example.com"}
        resp = self.client.post(url, data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_duplicate_email(self):
        url = reverse("employee-list")
        data = {"name": "A", "email": "dup@example.com"}
        resp1 = self.client.post(url, data, format="json")
        self.assertEqual(resp1.status_code, status.HTTP_201_CREATED)
        resp2 = self.client.post(url, data, format="json")
        self.assertEqual(resp2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_nonexistent(self):
        url = reverse("employee-detail", args=[9999])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)
