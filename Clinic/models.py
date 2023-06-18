from django.db import models
class Clinic(models.Model):
    Name=models.CharField(max_length=200,unique=True)
    Address=models.CharField(max_length=300)
    Contact=models.CharField(max_length=100)
    Email=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.Name
