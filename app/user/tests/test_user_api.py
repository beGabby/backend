from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """TEST the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    
    def test_create_valid_user_succes(self):
        """test creating user with valid payload is succesful"""
        payload = {
            "email": "tedst@londonappdev.com",
            "name": "angel",
            "password":"warszawa",
            "age": 23,
            "interestings": [
                "admin",
                "editor",
                "contributor"
                ],
            "languages": [ "{\"language\": \"english\", \"level\": \"native\"}", "{\"language\": \"english\", \"level\": \"native\"}" ]}

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)


    def test_user_exists(self):
        """test creating user that already exists fails"""
        payload = {
            "email": "tedst@londonappdev.com",
            "name": "angel",
            "password":"warszawa",
            "age": 23,
            "interestings": [
                "admin",
                "editor",
                "contributor"
                ],
            "languages": [ "{\"language\": \"english\", \"level\": \"native\"}", "{\"language\": \"english\", \"level\": \"native\"}" ]}

        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_password_too_short(self):
        """Test that password must be more than 5 characters"""
        payload = {
            "email": "tedst@londonappdev.com",
            "name": "angel",
            "password":"s",
            "age": 23,
            "interestings": [
                "admin",
                "editor",
                "contributor"
                ],
            "languages": [ "{\"language\": \"english\", \"level\": \"native\"}", "{\"language\": \"english\", \"level\": \"native\"}" ]}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email = payload['email']
        ).exists()
        self.assertFalse(user_exists)



