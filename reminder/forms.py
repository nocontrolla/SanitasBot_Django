from django import forms
from .models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient_doctor', 'medicine', 'dosage', 'start_date', 'end_date', 'additional_info']
