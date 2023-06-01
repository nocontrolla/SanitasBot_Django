from django.db import models
from hospitalregister.models import Patient, Doctor


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)
    description = models.CharField(max_length=255)
    

    def __str__(self):
        return "Patient - {} Doc- {} At {} {}".format(self.patient, self.doctor, self.date, self.time)


class Feedback(models.Model):
    # Define fields for Feedback
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    feedback_text = models.TextField()