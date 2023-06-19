
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from Patient.models import Patient
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import AllowAny


class clinic_detail(APIView):
    def get_object(self, pk):
        try:
            return Clinic.objects.get(pk=pk)
        except Clinic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        clinic = self.get_object(pk)
        serializer = ClinicSerializer(clinic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        clinic = self.get_object(pk)

        serializer = ClinicSerializer(clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        clinic = self.get_object(pk)
        clinic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes([AllowAny,])
class ClinicList(APIView):
    def get(self,request):
        clinics = Clinic.objects.all()
        data=ClinicSerializer(clinics,many=True).data
        return Response(data)
    def post(self,request):
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ClinicDetailsByPat(request,patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            clinic=Clinic.objects.get(pk=patient.Physio_Patient.Clinic_Physio.pk)
        except Clinic.DoesNotExist:
            return Response({'message': 'The Clinic does not exist'}, status=status.HTTP_404_NOT_FOUND)
        clinic_serializer = ClinicSerializer(clinic)
        return Response(clinic_serializer.data)

