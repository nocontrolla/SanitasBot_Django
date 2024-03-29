from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    
    path("admin-prescription", views.admin_prescription),
    path("admin-add-medicine", views.admin_add_medicine),
    
    path('admin-view-prescription', views.create_prescription , name='admin-view-presciption'),
    path("admin-medical-information", views.admin_medical_information, name='admin-medical-information'),
    path("admin-add-symptom", views.admin_add_symptom, name='admin-add-symptom'),
    path("admin-add-disease", views.admin_add_disease, name='admin-add-disease'),
    path("admin-view-symptoms", views.admin_view_symptoms, name='admin-view-symptoms'),
    path("admin-view-diseases", views.admin_view_diseases, name='admin-view-diseases'),
    
    path("add-prescription", views.create_prescription, name='add-presciption'),
    path("remove-prescription", views.delete_prescription, name='remove-prescription'),

    path("doctor-view-prescription", views.doctor_view_prescription, name='doctor-view-prescription'),
    path("patient-view-prescription", views.patient_view_prescription, name='patient-view-prescription'),
    path("view-prescription", views.view_prescription, name='view-prescription'),
    path("list-medicines", views.list_medicines, name='list-medicines'),

    path("search-medicine-view", views.search_medicine_view)

    
]
