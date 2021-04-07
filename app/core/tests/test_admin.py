from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):

        email = 'test@GMail.GOV.pl'
        age = 23
        interestings = ['sport', 'speedway']
        languages = {
                'pierwszy': 'pierwszy',
            }
        password = 'Password'

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser('admin@gov.pl','test123')

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email=email,
            age = age,
            interestings = interestings,
            languages = languages,
            password=password  
        )


    def test_users_listed(self):
        """Test that user are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        print(res)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.age)
        self.assertContains(res, self.user.interestings[0])
        self.assertContains(res, 'speedway')
        self.assertContains(res, self.user.languages['pierwszy'])


    def test_user_change_page(self):
        """test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        #/admin/core/user/id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    
    def test_create_user_page(self):
        """test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)




