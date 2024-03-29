from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor
from reminder import models
    
#for admin signup
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


#for student related form
class DoctorUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput(),
        }
    
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(char.isalnum() for char in password):
    #         raise forms.ValidationError('Password must be at least 8 characters long and contain letters, numbers, and symbols.')
    #     return password


class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['address','mobile','department','status','profile_pic']



#for teacher related form
class PatientUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['first_name','last_name','username','password', 'email']
        widgets = {
        'password': forms.PasswordInput()
        }

class DoctorPatientForm(forms.ModelForm):
    class Meta:
        model = models.DoctorPatient
        fields=['patientId','assignedDoctor','admission_date', 'end_admission', ]
        

class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    # assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','profile_pic']


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    
    
class PatientSymptomForm(forms.ModelForm):
        class Meta:
            model = models.PatientSymptom
            fields = ['patient', 'symptom', 'observed_date', 'duration_days', 'severity_level']
    
    

class PatientDiseaseForm(forms.ModelForm):
        class Meta:
            model = models.PatientDisease
            fields = ['patient', 'disease', 'diagnosis_date']