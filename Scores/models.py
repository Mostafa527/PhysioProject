from django.db import models
from Session.models import Session

class Scores(models.Model):
    DateOfCreation=models.DateTimeField(blank=True,null=True)
    ScorePoints=models.PositiveIntegerField(blank=False)
    PainAngles=models.CharField(max_length=300,blank=False)
    Session_Status=models.CharField(max_length=50,blank=False)
    Percentage=models.CharField(max_length=30,blank=False)
    Session_Score=models.ForeignKey(Session,related_name='session_score',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)