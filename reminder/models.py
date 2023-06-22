from django.db import models
from hospitalregister.models import Patient, DoctorPatient

dosages=[('1 X 1','1 X 1'),
         ('1 X 2','1 X 2'),
         ('1 X 3','1 X 3'),
         ('2 X 1','2 X 1'),
         ('2 X 2','2 X 2'),
         ('2 X 3','2 X 3'),
         ('3 X 1','3 X 1'),
         ('3 X 2','3 X 2'),
         ('3 X 3','3 X 3'),
]
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

    def __str__(self):
        return "Medication Name - {}".format(self.medication_name)

class Prescription(models.Model):
    patient_doctor = models.ForeignKey(DoctorPatient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE ,max_length=255, default=None)
    dosage = models.CharField(max_length=50, choices=dosages, default='1 X 3')
    frequency = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(auto_created=True)
    end_date = models.DateField(null=True)
    additional_info = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Presciption Doc-{} Patient-{}".format(self.patient_doctor.assignedDoctor.name, self.patient_doctor.patientId.name)