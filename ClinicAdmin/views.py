
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import AllowAny
from django.http import Http404

class admin_detail(APIView):
    def get_object(self, pk):
        try:
            return ClinicAdmin.objects.get(pk=pk)
        except ClinicAdmin.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print(snippet.pk)
        serializer = AdminProfileSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)

        serializer = AdminProfileSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@permission_classes([AllowAny,])
class adminList(APIView):
    def get(self,request):
        admins = ClinicAdmin.objects.all()
        data=AdminProfileSerializer(admins,many=True).data
        return Response(data)
    def post(self,request):
        serializer = AdminProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)