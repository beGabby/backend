from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_email_succesfull(self):
        """new user with email"""
        email = 'test@gov.pl'
        age = 23
        interestings = ['sport', 'speedway']
        languages = ['{"all":"perfect"}','{"all":"perfect"}']
        password = 'Password'

        user = get_user_model().objects.create_user(
            email=email,
            age = age,
            interestings = interestings,
            languages = languages,
            password=password,         
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalize(self):
        """normalize email"""
        email = 'test@GMail.GOV.pl'
        age = 23
        interestings = ['sport', 'speedway']
        languages = ['{"all":"perfect"}','{"all":"perfect"}']
        password = 'Password'

        user = get_user_model().objects.create_user(
            email=email,
            age = age,
            interestings = interestings,
            languages = languages,
            password=password         
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test user with wrong email"""
        
        with self.assertRaises(ValueError):
        
            email = 'GMail.GOV.pl'
            age = 23
            interestings = ['sport', 'speedway']
            languages = ['{"all":"perfect"}','{"all":"perfect"}',]
            password = "DzienDObry"
            user = get_user_model().objects.create_user(
                email=None,
                age = age,
                interestings = interestings,
                languages = languages,
                password=password,         
            )
    

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@gov.pl',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

