from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from hospitalregister.views import home_view, adminclick_view, doctorclick_view, patientclick_view

testuser='prayer'
testpassword='123456789'

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view_with_authenticated_user(self):
        user = User.objects.create_user(username=testuser, password=testpassword)
        self.client.force_login(user)
        response = self.client.get(reverse(''))
        self.assertRedirects(response, '/hospital/afterlogin')

    def test_home_view_with_anonymous_user(self):
        response = self.client.get(reverse('home_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/index.html')

# class AdminClickViewTest(TestCase):
#     def test_adminclick_view_with_authenticated_user(self):
#         user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client.force_login(user)
#         response = self.client.get(reverse('adminclick_view'))
#         self.assertRedirects(response, '/hospital/afterlogin')

#     def test_adminclick_view_with_anonymous_user(self):
#         response = self.client.get(reverse('adminclick_view'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'hospital/adminclick.html')

# class DoctorClickViewTest(TestCase):
#     def test_doctorclick_view_with_authenticated_user(self):
#         user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client.force_login(user)
#         response = self.client.get(reverse('doctorclick_view'))
#         self.assertRedirects(response, '/hospital/afterlogin')

#     def test_doctorclick_view_with_anonymous_user(self):
#         response = self.client.get(reverse('doctorclick_view'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'hospital/doctorclick.html')

# class PatientClickViewTest(TestCase):
#     def test_patientclick_view_with_authenticated_user(self):
#         user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client.force_login(user)
#         response = self.client.get(reverse('patientclick_view'))
#         self.assertRedirects(response, '/hospital/afterlogin')

#     def test_patientclick_view_with_anonymous_user(self):
#         response = self.client.get(reverse('patientclick_view'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'hospital/patientclick.html')
