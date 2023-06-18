from rest_framework import serializers
from .models import *


class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields= "__all__"