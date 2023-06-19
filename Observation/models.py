from django.db import models
from Session.models import Session
from Patient.models import Patient

class Observations(models.Model):
    DateOfCreation=models.DateField(blank=False)
    Notes=models.CharField(max_length=300)
    Session_Observation=models.ForeignKey(Session,related_name='session_observ',on_delete=models.CASCADE)
    Patient_Observation=models.ForeignKey(Patient,related_name='patient_observ',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)