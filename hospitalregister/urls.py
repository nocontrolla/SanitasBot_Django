from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [

    path('',views.home_view,name=''),
    path('about_us', views.aboutus_view, name='about_us'),
    path('contact_us', views.contactus_view, name='contact_us'),

    path('adminclick', views.adminclick_view, name='adminclick'),
    path('doctorclick', views.doctorclick_view, name='doctorclick'),
    path('patientclick', views.patientclick_view, name='patientclick'),

#-----------------------ADMIN_RELATED_URLS----------------------------------------------#
    path('adminsignup', views.admin_signup_view, name='adminsignup'),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view, name='patientsignup'),

    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html'), name='adminlogin'),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html'), name='adoctorlogin'),
    path('patientlogin', LoginView.as_view(template_name='hospital/patientlogin.html'), name='patientlogin'),
    path('admin-assign-doctor-patient', views.admin_assign_doctor_patient_view, name='admin-assign-doctor-patient'),
    path('doctor-patient-relation', views.doctor_patient_relation_view, name='doctor-patient-relation'),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view),

   
    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),

    

    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    # path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),

]

urlpatterns +=[
    
    path('doctor-assign-patient-disease', views.doctor_assign_patient_disease_view, name='doctor-assign-patient-disease'),
    path('doctor-assign-patient-symptom', views.doctor_assign_patient_symptom_view, name='doctor-assign-patient-symptom'),
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('search', views.search_view,name='search'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

]

urlpatterns +=[

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-view-doctor', views.patient_view_doctor_view,name='patient-view-doctor'),
    path('searchdoctor', views.search_doctor_view,name='searchdoctor'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'), 
    

]