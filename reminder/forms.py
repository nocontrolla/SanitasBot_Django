from django import forms
from .models import Prescription, Medicine, Disease, Symptom

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient_doctor', 'medicine', 'frequency', 'dosage', 'start_date', 'end_date', 'additional_info']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['medication_name', 'medicine_info']
        
        
class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = ['name', 'description']
        
        
class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['name', 'description']