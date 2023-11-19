from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User


class AccountTests(APITestCase):
    def test_create_account(self):
        url = reverse('user-register')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@test.com',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_password_mismatch(self):
        url = reverse('user-register')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'password2': 'differentpassword',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_fields(self):
        url = reverse('user-register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_existing_username(self):
        User.objects.create_user(username='existinguser', password='existingpassword')
        
        url = reverse('user-register')
        data = {
            'username': 'existinguser',
            'password': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_login(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        
        url = reverse('user-login')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Token', response.data)
