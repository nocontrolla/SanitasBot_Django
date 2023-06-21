from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("add-prescription", views.create_prescription),
    path("remove-prescription", views.delete_prescription),
    path("view-prescription", views.doctor_view_prescription),
    path("list-medicines", views.list_medicines),

    
]
