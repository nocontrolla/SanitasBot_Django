from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("add_prescription", views.create_prescription),
    path("remove_prescription", views.delete_prescription),
]
