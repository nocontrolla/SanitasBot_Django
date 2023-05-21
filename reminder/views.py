from django.shortcuts import render, redirect, get_object_or_404
from .models import Prescription
from .forms import PrescriptionForm
from hospitalregister import models

# Create your views here.
def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'reminder/prescription_list.html', {'prescriptions': prescriptions})

# In this example, the prescription_list view retrieves all the prescriptions from the database using Prescription.objects.all(). 
# Then it renders the prescription_list.html template, passing the retrieved prescriptions as context data.

def create_prescription(request):
    if request.method == 'POST':
        if isinstance(request.user, models.Doctor):  # Check if the user is a Doctor
            form = PrescriptionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('prescription_list')
        else:
            return redirect('prescription_list')  # Redirect if the user is not a Doctor
    else:
        form = PrescriptionForm()
    return render(request, 'reminder/create_prescription.html', {'form': form})


def delete_prescription(request, prescription_id):
    if isinstance(request.user, models.Doctor):  # Check if the user is a Doctor
        prescription = get_object_or_404(Prescription, id=prescription_id)
        prescription.delete()
    return redirect('prescription_list')

