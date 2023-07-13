from django.shortcuts import render,redirect,reverse
from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
# from datetime import datetime,timedelta,date
from django.conf import settings
from django.db.models import Q
from hospitalregister import views, models
from hospitalregister.models import User
from appointment import models


@login_required(login_url='hospital/doctorlogin')
@user_passes_test(views.is_doctor)
def doctor_approve_appointment_view(request):
    #those whose approval are needed
    appointments=models.Appointment.objects.all().filter(status=False)
    patients = models.Patient.objects.all()
    doctors = models.Doctor.objects.all()
    
    mydict={'appointments':appointments, 'patients':patients, 'doctors':doctors}   
    return render(request,'appointment/doctor_approve_appointment.html', mydict)



@login_required(login_url='hospital/doctorlogin')
@user_passes_test(views.is_doctor)
def docapprove_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect(reverse('doctor-approve-appointment'))



@login_required(login_url='hospital/doctorlogin')
@user_passes_test(views.is_doctor)
def docreject_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('doctor-approve-appointment')


@login_required(login_url='hospital/doctorlogin')
@user_passes_test(views.is_doctor)
def doctor_appointment_view(request): 
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'appointment/doctor_appointment.html',{'doctor':doctor})


@login_required(login_url='hospital/patientlogin')
@user_passes_test(views.is_patient)
def patient_view_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    
    appointments=models.Appointment.objects.all().filter(patient=request.user.id)
    doctor = models.Doctor.objects.all()
    
    return render(request,'appointment/patient_view_appointment.html',{'appointments':appointments,'doctor':doctor})



@login_required(login_url='hospital/doctorlogin')
@user_passes_test(views.is_doctor)
def doctor_view_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True, doctor=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patient_id)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'appointment/doctor_view_appointment.html',{'appointments':appointments,'doctor':doctor})



@login_required(login_url='hospital/doctorlogin')
@user_passes_test(views.is_doctor)
def doctor_delete_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctor=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'appointment/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})



@login_required(login_url='hospital/doctorlogin')
@user_passes_test(views.is_doctor)
def delete_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctor=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'appointment/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})




@login_required(login_url='hospital/patientlogin')
@user_passes_test(views.is_patient)
def patient_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'appointment/patient_appointment.html',{'patient':patient})




@login_required(login_url='hospital/patientlogin')
@user_passes_test(views.is_patient)
def patient_book_appointment_view(request):
    appointmentForm=forms.PatientAppointmentForm
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    message=None
    mydict={'appointmentForm':appointmentForm, 'patient':patient,'message':message}
    if request.method=='POST':
        appointmentForm=forms.PatientAppointmentForm(request.POST)
        if appointmentForm.is_valid():
            desc=request.POST.get('description')
            
            doctor=models.Doctor.objects.get(user_id=request.POST.get('doctor'))
            patient = models.Patient.objects.get(user_id=request.user.id)
            appointment=appointmentForm.save(commit=False)
            appointment.doctor=request.POST.get('doctor')
            appointment.patient=request.user.id
            appointment.status=False
            appointment.save()
        return HttpResponseRedirect(reverse('patient-view-appointment'))
    
    return render(request,'appointment/patient_book_appointment.html',context=mydict)



@login_required(login_url='hospital/adminlogin')
@user_passes_test(views.is_admin)
def admin_appointment_view(request):
    return render(request,'appointment/admin_appointment.html')



@login_required(login_url='hospital/adminlogin')
@user_passes_test(views.is_admin)
def admin_view_appointment_view(request):
    appointments=models.Appointment.objects.all().filter(status=True)
    
    patients = models.Patient.objects.all()
    doctors = models.Doctor.objects.all()
    
    mydict={'appointments':appointments, 'patients':patients, 'doctors':doctors} 
    return render(request,'appointment/admin_view_appointment.html', mydict)



@login_required(login_url='hospital/adminlogin')
@user_passes_test(views.is_admin)
def admin_add_appointment_view(request):
    appointmentForm=forms.AppointmentForm
    mydict={'appointmentForm':appointmentForm,}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctor=request.POST.get('doctor')
            appointment.patient=request.POST.get('patient')
            appointment.status=True
            appointment.save()
        return HttpResponseRedirect(reverse('admin-view-appointment'))
    return render(request,'appointment/admin_add_appointment.html',context=mydict)



@login_required(login_url='hospital/adminlogin')
@user_passes_test(views.is_admin)
def admin_approve_appointment_view(request):
    #those whose approval are needed
    appointments=models.Appointment.objects.all().filter(status=False)
    
    doctor = models.Doctor.objects.all()
    patient = models.Patient.objects.all()
    
    return render(request,'appointment/admin_approve_appointment.html',{'appointments':appointments, 'patient': patient, 'doctor': doctor})



@login_required(login_url='hospital/adminlogin')
@user_passes_test(views.is_admin)
def approve_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect(reverse('admin-approve-appointment'))



@login_required(login_url='hospital/adminlogin')
@user_passes_test(views.is_admin)
def reject_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('admin-approve-appointment')
#-------------------------------------------------------

