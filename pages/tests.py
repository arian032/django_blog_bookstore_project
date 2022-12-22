from django.test import TestCase

from django.shortcuts import reverse


class TestPage(TestCase):

    # test urls
    def test_home_page_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_url(self):
        response = self.client.get('/about_us/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_by_url_name(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)

    # test templates
    def test_home_page_templates(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_template_by_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_aboutus_page_templates(self):
        response = self.client.get('/about_us/')
        self.assertTemplateUsed(response, 'page/about_us.html')

    def test_aboutus_page_template_by_url_name(self):
        response = self.client.get(reverse('about_us'))
        self.assertTemplateUsed(response, 'page/about_us.html')
