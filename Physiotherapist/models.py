from django.db import models
from Clinic.models import Clinic
from Accounts.models import NewUser
class Physiotherapist(models.Model):

    user = models.OneToOneField(NewUser,on_delete=models.CASCADE, primary_key=True, related_name='physio_user')

    Clinic_Physio=models.ForeignKey(Clinic,related_name='pysio_therpists',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
