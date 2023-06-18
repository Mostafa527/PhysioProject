from django.db import models
from Clinic.models import Clinic
from Accounts.models import NewUser
class ClinicAdmin(models.Model):
    #Inherited from NewUser Class
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True, related_name='admin_user')
    #Relationship between Admin and Clinic is One-To-Many
    Admin_Clinic =models.ForeignKey(Clinic,related_name='admins',on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
