from django.test import TestCase
from django.urls import reverse, resolve
from hospitalregister import admin, views

class HospitalRegisterURLTest(TestCase):
    def test_home_view_url(self):
        url = reverse('')
        self.assertEqual(resolve(url).func, views.home_view)

    def test_aboutus_view_url(self):
        url = reverse('about_us')
        self.assertEqual(resolve(url).func, views.aboutus_view)

    def test_contactus_view_url(self):
        url = reverse('contact_us')
        self.assertEqual(resolve(url).func, views.contactus_view)

    def test_adminclick_view_url(self):
        url = reverse('adminclick')
        self.assertEqual(resolve(url).func, views.adminclick_view)

    def test_doctorclick_view_url(self):
        url = reverse('doctorclick')
        self.assertEqual(resolve(url).func, views.doctorclick_view)

    def test_patientclick_view_url(self):
        url = reverse('patientclick')
        self.assertEqual(resolve(url).func, views.patientclick_view)

    # Add more tests for other URLs in the hospitalregister.urls module

