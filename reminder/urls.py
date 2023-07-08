from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("add-prescription", views.create_prescription),
    path("remove-prescription", views.delete_prescription),

    path("doctor-view-prescription", views.doctor_view_prescription, name='doctor-view-prescription'),
    path("patient-view-prescription", views.patient_view_prescription),
    path("view-prescription", views.view_prescription),
    path("list-medicines", views.list_medicines),

    path("search-medicine-view", views.search_medicine_view)

    
]
