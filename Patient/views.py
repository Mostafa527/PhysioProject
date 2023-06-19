
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404

class patient_detail(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        print(patient.pk)
        serializer = PatientProfileSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = self.get_object(pk)

        serializer = PatientProfileSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientList(APIView):
    def get(self,request):
        patients = Patient.objects.all()
        data=PatientProfileSerializer(patients,many=True).data
        return Response(data)
    def post(self,request):
        serializer = PatientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def PatientsDetailsByTherpy(request,physio_id):
    try:
        physiotherapist = Physiotherapist.objects.get(pk=physio_id)
    except Physiotherapist.DoesNotExist:
        return Response({'message': 'The Physiotherapist does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            patient=physiotherapist.patients.all()
        except Patient.DoesNotExist:
            return Response({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)
        patient_serializer = PatientProfileSerializer(patient,many=True)
        return Response(patient_serializer.data)