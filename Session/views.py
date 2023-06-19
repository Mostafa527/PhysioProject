
from rest_framework import status
from rest_framework.response import Response
from ExercisePlan.models import Exercise_Plan
from .models import Session
from .serializers import SessionSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
@api_view(['GET'])
def SessionByExercisePlan(request,exerciseplan_id):
    try:
        exercise_plan = Exercise_Plan.objects.get(pk=exerciseplan_id)
    except Exercise_Plan.DoesNotExist:
        return Response({'message': 'The ExercisePlan does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            session=exercise_plan.session_plan.all()
        except Session.DoesNotExist:
            return Response({'message': 'The Session does not exist'}, status=status.HTTP_404_NOT_FOUND)
        session_serializer =SessionSerializer(session,many=True)
        return Response(session_serializer.data)


class SessionList(APIView):
    def get(self,request):
        sessions = Session.objects.all()
        data=SessionSerializer(sessions,many=True).data
        return Response(data)
    def post(self,request):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def session_detail(request, session_id):
    try:
        session =Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        return Response({'message': 'No Sessions'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        session_serializer = SessionSerializer(session)
        return Response(session_serializer.data)
