from django.shortcuts import render,redirect,reverse
from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from django.db.models import Q
from appointment.models import Appointment
from hospitalregister.models import Doctor, DoctorPatient, Patient, PatientDischargeDetails, User
# from django.contrib.auth import get_user_model
# Create your views here.

# User = get_user_model()

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/hospital/afterlogin')
    return render(request,'hospital/index.html')


#for showing signup/login button for admin(by bgame)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/hospital/afterlogin')
    return render(request,'hospital/adminclick.html')


#for showing signup/login button for doctor(by bgame)
def doctorclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/hospital/afterlogin')
    return render(request,'hospital/doctorclick.html')


#for showing signup/login button for patient(by bgame)
def patientclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/hospital/afterlogin')
    return render(request,'hospital/patientclick.html')


# def admin_signup_view(request):
#     form = forms.AdminSignupForm()
#     if request.method == 'POST':
#         form = forms.AdminSignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             # email = form.cleaned_data['email']

#             # Check if username or email already exists in the database
#             if models.User.objects.filter(username=username).exists():
#                 form.add_error('username', 'Username already exists')
#             # elif User.objects.filter(email=email).exists():
#             #     form.add_error('email', 'Email already exists')
#             else:
#                 user = form.save(commit=False)
#                 user.set_password(user.password)
#                 user.save()
#                 my_admin_group, _ = Group.objects.get_or_create(name='ADMIN')
#                 my_admin_group[0].user_set.add(user)
#             return HttpResponseRedirect('/hospital/adminlogin')

#     return render(request, 'hospital/adminsignup.html', {'form': form})
def admin_signup_view(request):
    form=forms.AdminSignupForm()
    if request.method=='POST':
        form=forms.AdminSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('/hospital/adminlogin')
    return render(request,'hospital/adminsignup.html',{'form':form})




# def doctor_signup_view(request):
#     userForm = forms.DoctorUserForm()
#     doctorForm = forms.DoctorForm()
#     mydict = {'userForm': userForm, 'doctorForm': doctorForm}
    
#     if request.method == 'POST':
#         userForm = forms.DoctorUserForm(request.POST)
#         doctorForm = forms.DoctorForm(request.POST, request.FILES)
        
#         if userForm.is_valid() and doctorForm.is_valid():
#             username = userForm.cleaned_data['username']
#             email = userForm.cleaned_data['email']

#             # Check if username or email already exists in the database
#             if User.objects.filter(username=username).exists():
#                 userForm.add_error('username', 'Username already exists')
#             elif User.objects.filter(email=email).exists():
#                 userForm.add_error('email', 'Email already exists')
#             else:
#                 user = userForm.save()
#                 user.set_password(user.password)
#                 user.save()
#                 doctor = doctorForm.save(commit=False)
#                 doctor.user = user
#                 doctor.save()
#                 my_doctor_group, _ = Group.objects.get_or_create(name='DOCTOR')
#                 my_doctor_group[0].user_set.add(user)
#         return HttpResponseRedirect('/hospital/doctorlogin')
    
#     return render(request, 'hospital/doctorsignup.html', context=mydict)
def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)

        if userForm.is_valid() and doctorForm.is_valid():
            
            password = userForm.cleaned_data['password']
            confirm_password = userForm.cleaned_data['confirm_password']

            if password == confirm_password:
                user=userForm.save()
                user.set_password(user.password)
                user.save()

                doctor=doctorForm.save(commit=False)
                doctor.user=user
                doctor=doctor.save()
                
                my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
                my_doctor_group[0].user_set.add(user)
            else:
                messages.error(request, 'Passwords do not match.')                
        return HttpResponseRedirect('/hospital/doctorlogin')
    return render(request,'hospital/doctorsignup.html',context=mydict)


def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)

        if userForm.is_valid() and patientForm.is_valid():
            password = userForm.cleaned_data['password']
            confirm_password = userForm.cleaned_data['confirm_password']

            if password == confirm_password:
                user=userForm.save()
                user.set_password(user.password)
                user.save()
                patient=patientForm.save(commit=False)
                patient.user=user
                # patient.assignedDoctor=request.POST.get('assignedDoctorId')
                patient=patient.save()
                my_patient_group = Group.objects.get_or_create(name='PATIENT')
                my_patient_group[0].user_set.add(user)
            else:
                messages.error(request, 'Passwords do not match.')
        return HttpResponseRedirect('/hospital/patientlogin')
    return render(request, 'hospital/patientsignup.html',context=mydict)


#-----------for checking user is doctor , patient or admin(by bgame)
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
    
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('/hospital/admin-dashboard')
    
    elif is_doctor(request.user):
        accountapproval=Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('/hospital/doctor-dashboard')
        else:
            return render(request,'hospital/doctor_wait_for_approval.html')
        
    elif is_patient(request.user):
        accountapproval=Patient.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('/hospital/patient-dashboard')
        else:
            return render(request,'hospital/patient_wait_for_approval.html')
        

    # return redirect('/hospital/admin-dashboard')


#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    doctors=Doctor.objects.all().order_by('-id')
    patients=Patient.objects.all().order_by('-id')
    #for three cards
    doctorcount=Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=Doctor.objects.all().filter(status=False).count()

    patientcount=Patient.objects.all().filter(status=True).count()
    pendingpatientcount=Patient.objects.all().filter(status=False).count()

    appointmentcount=Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=Appointment.objects.all().filter(status=False).count()
    mydict={
    'doctors':doctors,
    'patients':patients,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'hospital/admin_dashboard.html',context=mydict)


# this view for sidebar click on admin page
@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_doctor_view(request):
    return render(request,'hospital/admin_doctor.html')



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_view(request):
    doctors=Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor.html',{'doctors':doctors})



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def delete_doctor_from_hospital_view(request,pk):
    doctor=Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin-view-doctor')



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def update_doctor_view(request,pk):
    doctor=Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)

    userForm=forms.DoctorUserForm(instance=user)
    doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST,instance=user)
        doctorForm=forms.DoctorForm(request.POST,request.FILES,instance=doctor)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.status=True
            doctor.save()
            return redirect('admin-view-doctor')
    return render(request,'hospital/admin_update_doctor.html',context=mydict)




@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_add_doctor_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.status=True
            doctor.save()

            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-doctor')
    return render(request,'hospital/admin_add_doctor.html',context=mydict)




@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_approve_doctor_view(request):
    #those whose approval are needed
    doctors=Doctor.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_doctor.html',{'doctors':doctors})


@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def approve_doctor_view(request,pk):
    doctor=Doctor.objects.get(id=pk)
    doctor.status=True
    doctor.save()
    return redirect(reverse('admin-approve-doctor'))


@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def reject_doctor_view(request,pk):
    doctor=Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin-approve-doctor')



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_specialisation_view(request):
    doctors=Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor_specialisation.html',{'doctors':doctors})



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request,'hospital/admin_patient.html')



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_view_patient_view(request):
    patients=Patient.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_patient.html',{'patients':patients})



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def delete_patient_from_hospital_view(request,pk):
    patient=Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-view-patient')



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def update_patient_view(request,pk):
    patient=Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientUserForm(instance=user)
    patientForm=forms.PatientForm(request.FILES,instance=patient)
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST,instance=user)
        patientForm=forms.PatientForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.status=True
            # patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()
            return redirect('admin-view-patient')
    return render(request,'hospital/admin_update_patient.html',context=mydict)





@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_add_patient_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            patient=patientForm.save(commit=False)
            patient.user=user
            patient.status=True
            patient.save()

            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-patient')
    return render(request,'hospital/admin_add_patient.html',context=mydict)



#------------------FOR APPROVING PATIENT BY ADMIN----------------------
@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def admin_approve_patient_view(request):
    #those whose approval are needed
    patients=Patient.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_patient.html',{'patients':patients})



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def approve_patient_view(request,pk):
    patient=Patient.objects.get(id=pk)
    patient.status=True
    patient.save()
    return redirect(reverse('admin-approve-patient'))



@login_required(login_url='hospital/adminlogin')
@user_passes_test(is_admin)
def reject_patient_view(request,pk):
    patient=Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-approve-patient')



#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='hospital/doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    #for three cards
    patientcount=Patient.objects.all().filter(status=True,assignedDoctor_id=request.user.id).count()
    appointmentcount=Appointment.objects.all().filter(status=True,doctor_id=request.user.id).count()
    patientdischarged=PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name).count()

    #for  table in doctor dashboard
    appointments=Appointment.objects.all().filter(status=True,doctor_id=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    mydict={
    'patientcount':patientcount,
    'appointmentcount':appointmentcount,
    'patientdischarged':patientdischarged,
    'appointments':appointments,
    'doctor':Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_dashboard.html',context=mydict)



@login_required(login_url='hospital/doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_view(request):
    mydict={
    'doctor':Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_patient.html',context=mydict)





@login_required(login_url='hospital/doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_patient_view(request):
    patients=Patient.objects.all().filter(status=True,assignedDoctor_id=request.user.id)
    doctor=Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_view_patient.html',{'patients':patients,'doctor':doctor})


@login_required(login_url='hospital/doctorlogin')
@user_passes_test(is_doctor)
def search_view(request):
    doctor=Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    # whatever user write in search box we get in query
    query = request.GET['query']
    patients=Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id).filter(Q(symptoms__icontains=query)|Q(user__first_name__icontains=query))
    return render(request,'hospital/doctor_view_patient.html',{'patients':patients,'doctor':doctor})



@login_required(login_url='hospital/doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_discharge_patient_view(request):
    dischargedpatients=PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name)
    doctor=Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_view_discharge_patient.html',{'dischargedpatients':dischargedpatients,'doctor':doctor})




#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------





#--------------------- FOR DISCHARGING PATIENT BY ADMIN START-------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_discharge_patient_view(request):
    patients=Patient.objects.all().filter(status=True)
    return render(request,'hospital/admin_discharge_patient.html',{'patients':patients})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def discharge_patient_view(request,pk):
    patient=Patient.objects.get(id=pk)
    days=(date.today()-patient.admitDate) #2 days, 0:00:00
    assignedDoctor=models.User.objects.all().filter(id=patient.assignedDoctorId)
    d=days.days # only how many day that is 2
    patientDict={
        'patientId':pk,
        'name':patient.get_name,
        'mobile':patient.mobile,
        'address':patient.address,
        'symptoms':patient.symptoms,
        'admitDate':patient.admitDate,
        'todayDate':date.today(),
        'day':d,
        'assignedDoctorName':assignedDoctor[0].first_name,
    }
    if request.method == 'POST':
        feeDict ={
            'roomCharge':int(request.POST['roomCharge'])*int(d),
            'doctorFee':request.POST['doctorFee'],
            'medicineCost' : request.POST['medicineCost'],
            'OtherCharge' : request.POST['OtherCharge'],
            'total':(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
        }
        patientDict.update(feeDict)
        #for updating to database patientDischargeDetails (pDD)
        pDD=PatientDischargeDetails()
        pDD.patientId=pk
        pDD.patientName=patient.get_name
        pDD.assignedDoctorName=assignedDoctor[0].first_name
        pDD.address=patient.address
        pDD.mobile=patient.mobile
        pDD.symptoms=patient.symptoms
        pDD.admitDate=patient.admitDate
        pDD.releaseDate=date.today()
        pDD.daySpent=int(d)
        pDD.medicineCost=int(request.POST['medicineCost'])
        pDD.roomCharge=int(request.POST['roomCharge'])*int(d)
        pDD.doctorFee=int(request.POST['doctorFee'])
        pDD.OtherCharge=int(request.POST['OtherCharge'])
        pDD.total=(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
        pDD.save()
        return render(request,'hospital/patient_final_bill.html',context=patientDict)
    return render(request,'hospital/patient_generate_bill.html',context=patientDict)



#---------------------------------------------------------------------------------
#------------------------ PATIENT RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='hospital/patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient=Patient.objects.get(user_id=request.user.id)
    patient_intermediate=DoctorPatient.objects.get(patientId_id=patient.id)
    doctor=Doctor.objects.get(id=patient_intermediate.assignedDoctor_id)
    mydict={
    'patient':patient,
    'doctorName':doctor.get_name,
    'doctorMobile':doctor.mobile,
    'doctorAddress':doctor.address,
    'doctorDepartment':doctor.department,
    # 'admitDate':patient.admission_date,
    }
    return render(request,'hospital/patient_dashboard.html',context=mydict)

def patient_view_doctor_view(request):
    doctors=Doctor.objects.all().filter(status=True)
    patient=Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'hospital/patient_view_doctor.html',{'patient':patient,'doctors':doctors})



def search_doctor_view(request):
    patient=Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    
    # whatever user write in search box we get in query
    query = request.GET['query']
    doctors=Doctor.objects.all().filter(status=True).filter(Q(department__icontains=query)| Q(user__first_name__icontains=query))
    return render(request,'hospital/patient_view_doctor.html',{'patient':patient,'doctors':doctors})





#--------------------------------------------------------------------------------
#------------------------ PATIENT RELATED VIEWS END ------------------------------
#--------------------------------------------------------------------------------





#---------------------------------------------------------------------------------
#------------------------ ABOUT US AND CONTACT US VIEWS START ------------------------------
#---------------------------------------------------------------------------------
def aboutus_view(request):
    return render(request,'hospital/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'hospital/contactussuccess.html')
    return render(request, 'hospital/contactus.html', {'form':sub})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_discharge_view(request):
    patient=Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    dischargeDetails=PatientDischargeDetails.objects.all().filter(patientId=patient.id).order_by('-id')[:1]
    patientDict=None
    if dischargeDetails:
        patientDict ={
        'is_discharged':True,
        'patient':patient,
        'patientId':patient.id,
        'patientName':patient.get_name,
        'assignedDoctorName':dischargeDetails[0].assignedDoctorName,
        'address':patient.address,
        'mobile':patient.mobile,
        'symptoms':patient.symptoms,
        'admitDate':patient.admitDate,
        'releaseDate':dischargeDetails[0].releaseDate,
        'daySpent':dischargeDetails[0].daySpent,
        'medicineCost':dischargeDetails[0].medicineCost,
        'roomCharge':dischargeDetails[0].roomCharge,
        'doctorFee':dischargeDetails[0].doctorFee,
        'OtherCharge':dischargeDetails[0].OtherCharge,
        'total':dischargeDetails[0].total,
        }
        print(patientDict)
    else:
        patientDict={
            'is_discharged':False,
            'patient':patient,
            'patientId':request.user.id,
        }
    return render(request,'hospital/patient_discharge.html',context=patientDict)


