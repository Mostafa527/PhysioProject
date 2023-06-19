from django.db import models
from Accounts.models import NewUser
class Game(models.Model):
    Name=models.CharField(max_length=80,unique=True)
    Description=models.CharField(max_length=250)
    owner =models.ForeignKey(NewUser,related_name='Game_Owner',on_delete=models.CASCADE)

    def __str__(self):
        return self.Name