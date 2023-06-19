from rest_framework import serializers
from .models import *
class Exercise_Plan_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise_Plan
        fields = "__all__"