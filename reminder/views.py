from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Prescription
from .forms import PrescriptionForm, MedicineForm, SymptomForm, DiseaseForm
from hospitalregister.models import Doctor
from . import models

# Create your views here.
def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'reminder/prescription_list.html', {'prescriptions': prescriptions})

# In this example, the prescription_list view retrieves all the prescriptions from the database using Prescription.objects.all(). 
# Then it renders the prescription_list.html template, passing the retrieved prescriptions as context data.
@login_required(login_url='hospital/adminlogin')
def admin_prescription(request):
    return render(request, 'reminder/admin_prescription.html')


@login_required(login_url='hospital/adminlogin')
def admin_add_medicine(request):
    medicineform = MedicineForm()
    
    mydict={'medicineform':medicineform,}
    if request.method == 'POST':
        medicineform = MedicineForm(request.POST)
        if medicineform.is_valid():
            medicineform.save()
            return HttpResponseRedirect('admin-prescription')
    else:
        form = MedicineForm()
        
    return render(request, 'reminder/add_new_medicine.html', context=mydict, )


# @login_required(login_url='hospital/adminlogin')
@login_required(login_url='hospital/doctorlogin')
def create_prescription(request):
    prescriptionform = PrescriptionForm()
    mydict={'prescriptionform':prescriptionform,}
    
    if request.method == 'POST':  # Check if the user is a Doctor
        prescriptionform = PrescriptionForm(request.POST)
        if prescriptionform.is_valid():
            prescriptionform.save()
            return redirect('doctor-view-prescription')  # Redirect if the user is not a Doctor
    else:
        form = PrescriptionForm()
    return render(request, 'reminder/create_prescription.html', context=mydict,)


def delete_prescription(request, prescription_id):
    if isinstance(request.user, models.Doctor):  # Check if the user is a Doctor
        prescription = get_object_or_404(Prescription, id=prescription_id)
        prescription.delete()
    return redirect('prescription_list')

def doctor_view_prescription(request):


    return render(request, 'reminder/doctor_prescription.html')


def patient_view_prescription(request):
    return render(request, 'reminder/patient_prescription.html')



def list_medicines(request):
    medicines = models.Medicine.objects.all()

    return render(request, 'reminder/patient_list_medicine.html', {'medicines': medicines})


def view_prescription(request):
    # patient = request.user  # Assuming the authenticated user is the patient
    this = request.user
    patient = models.Patient.objects.get(user_id=this)
    doctor_patient = models.DoctorPatient.objects.get(patientId_id = patient.id)

    prescriptions = Prescription.objects.filter(patient_doctor_id=doctor_patient.id)

    medicines = models.Medicine.objects.all()

    return render(request, 'reminder/view_prescription.html', {'prescriptions': prescriptions , 'medicines': medicines})


def search_medicine_view(request):
    # patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    
    # whatever user write in search box we get in query
    query = request.GET['query']
    medicines = models.Medicine.objects.all().filter().filter(Q(medication_name__icontains=query)| Q(medicine_info__icontains=query))

    return render(request,'reminder/patient_list_medicine.html',{'patient':patient,'medicines':medicines})

def admin_medical_information(request):
    return render(request, 'reminder/admin_medical_information.html')





def admin_add_symptom(request):
    symptom = SymptomForm()
    
    mydict={'symptom':symptom,}
    
    if request.method == 'POST':  # Check if the user is a Doctor
        symptom = SymptomForm(request.POST)
        if symptom.is_valid():
            symptom.save()
            return redirect('/reminder/admin-view-symptoms')  # Redirect if the user is not a Doctor
    else:
        form = DiseaseForm()
    
    return render(request, 'reminder/admin_add_symptoms.html', context=mydict,)



def admin_view_symptoms(request):
    symptoms = models.Symptom.objects.all()
    
    return render(request, 'reminder/admin_view_symptoms.html', {'symptoms':symptoms})



def admin_view_diseases(request):
    diseases = models.Disease.objects.all()
        
    return render(request, 'reminder/admin_view_diseases.html', {'diseases':diseases})


def admin_add_disease(request):
    disease = DiseaseForm()
    
    mydict={'disease':disease,}
    
    if request.method == 'POST':  # Check if the user is a Doctor
        disease = DiseaseForm(request.POST)
        if disease.is_valid():
            disease.save()
            return redirect('/reminder/admin-view-diseases')  # Redirect if the user is not a Doctor
    else:
        form = MedicineForm()
    
    return render(request, 'reminder/admin_add_disease.html', context=mydict,)
    
