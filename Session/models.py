from django.db import models
from ExercisePlan.models import Exercise_Plan
class Session(models.Model):
    DateOfCreation=models.DateTimeField(blank=True,null=True)
    Session_Plan=models.ForeignKey(Exercise_Plan,related_name='session_plan',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)