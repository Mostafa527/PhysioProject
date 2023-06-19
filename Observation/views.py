
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Observations
from .serializers import ObservationSerializer
from Session.models import Session
from django.http import Http404


class observ_detail(APIView):
    def get_object(self, pk):
        try:
            return Observations.objects.get(pk=pk)
        except Observations.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        observ = self.get_object(pk)
        serializer = ObservationSerializer(observ)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        observ = self.get_object(pk)

        serializer = ObservationSerializer(observ, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        observ = self.get_object(pk)
        observ.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ObservationList(APIView):
    def get(self,request):
        observations = Observations.objects.all()
        data=ObservationSerializer(observations,many=True).data
        return Response(data)
    def post(self,request):
        serializer = ObservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ObservationDetailsBySession(request,session_id):
    try:
        session = Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        return Response({'message': 'The Session does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            observation=session.session_observ.all()
        except Observations.DoesNotExist:
            return Response({'message': 'No Observations is existed'}, status=status.HTTP_404_NOT_FOUND)
        observation_serializer = ObservationSerializer(observation,many=True)
        return Response(observation_serializer.data)
