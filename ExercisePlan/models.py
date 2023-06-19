from django.db import models
from Physiotherapist.models import Physiotherapist
from Patient.models import Patient
from Game.models import Game
class Exercise_Plan(models.Model):
    DateOfStart=models.DateField(blank=False)
    DateOfEnd=models.DateField(blank=False)
    RepitionNum = models.PositiveIntegerField(blank=False)
    LinkSide=models.CharField(max_length=50,blank=False)
    Angle=models.FloatField(blank=False)
    Difficulty=models.CharField(max_length=50)
    Notes=models.CharField(max_length=500)
    RestTime=models.PositiveIntegerField(blank=False)
    Physio_Exerplan=models.ForeignKey(Physiotherapist,related_name='Physio_Plan',on_delete=models.CASCADE)
    Patient_Exerplan=models.ForeignKey(Patient,related_name='Patient_Plan',on_delete=models.CASCADE)
    Game_Exerplan=models.ForeignKey(Game,related_name='Game_Plan',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)