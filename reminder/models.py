from django.db import models
from hospitalregister.models import Patient, Doctor


# Create your models here.
class Symptom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.name
    

class Disease(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class PatientDisease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    diagnosis_date = models.DateField()


class PatientSymptom(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    observed_date = models.DateField()
    duration_days = models.PositiveIntegerField(blank=True, null=True)
    severity_level = models.PositiveIntegerField(choices=[(1, 'Mild'), (2, 'Moderate'), (3, 'Severe')], blank=True, null=True, default='Mild')


class Medicine(models.Model):
    medication_name = models.TextField(null=True)
    medicine_info = models.TextField(null=True)

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE ,max_length=255, default=None)
    dosage = models.CharField(max_length=255, default='1 X 3')
    frequency = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(auto_created=True)
    end_date = models.DateField(null=True)
    additional_info = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Presciption Doc-{} Patient-{}".format(self.doctor, self.patient)
    