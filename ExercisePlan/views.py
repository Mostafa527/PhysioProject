
from rest_framework import status
from rest_framework.response import Response
from Patient.serializers import PatientProfileSerializer
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404

class exerciseplan_detail(APIView):
    def get_object(self, pk):
        try:
            return Exercise_Plan.objects.get(pk=pk)
        except Exercise_Plan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exercise_plan = self.get_object(pk)
        serializer = Exercise_Plan_Serializer(exercise_plan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exercise_plan = self.get_object(pk)

        serializer = Exercise_Plan_Serializer(exercise_plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        exercise_plan = self.get_object(pk)
        exercise_plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExercisePlanList(APIView):
    def get(self,request):
        exercises = Exercise_Plan.objects.all()
        data=Exercise_Plan_Serializer(exercises,many=True).data
        return Response(data)
    def post(self,request):
        serializer = Exercise_Plan_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ExercisePlanDetailsByPatient(request,patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            exercise_plan=patient.Patient_Plan.all()
        except Exercise_Plan.DoesNotExist:
            return Response({'message': 'No ExercisePlan Existed'}, status=status.HTTP_404_NOT_FOUND)
        exerciseplan_serializer = Exercise_Plan_Serializer(exercise_plan,many=True)
        return Response(exerciseplan_serializer.data)


@api_view(['GET'])
def ValidExercisePlanByPatient(request,physio_id):
    #Still want to Update
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


