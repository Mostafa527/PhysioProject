from django.db import models
from Physiotherapist.models import Physiotherapist
from Accounts.models import NewUser
class Patient(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True, related_name='patient_user')

    Physio_Patient=models.ForeignKey(Physiotherapist,related_name='patients',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username