from django.db import models
from hospitalregister.models import Patient, Doctor

# Create your models here.
class Appointment(models.Model):
    patient = models.PositiveIntegerField(null=True)
    doctor = models.PositiveIntegerField(null=True)
    date = models.DateField(blank=True)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=255)
    state = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending',max_length=20)
        
    def __str__(self):
        return "Patient - {} Doc- {} At {} from {} to {}".format(self.patient, self.doctor, self.date, self.start_time, self.end_time)


class Feedback(models.Model):
    # Define fields for Feedback
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    feedback_text = models.TextField()