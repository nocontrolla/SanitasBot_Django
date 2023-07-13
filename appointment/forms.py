from django import forms
from django.contrib.auth.models import User
from .models import Appointment
from hospitalregister import models


class AppointmentForm(forms.ModelForm):
    doctor=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="id")
    patient=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name", to_field_name="id")
    class Meta:
        model= Appointment
        fields=['date','start_time','end_time','description','status','state']


class PatientAppointmentForm(forms.ModelForm):
    doctor=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model= Appointment
        fields=['date','start_time','end_time','description','status','state']


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



#Developed By : Brian Godwin