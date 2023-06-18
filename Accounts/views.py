
from .serializers import *
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import  permission_classes
from django.http import Http404
@permission_classes([AllowAny,])
class RegisterView(APIView):
    def get(self, request):
        admins = NewUser.objects.all()
        data = UserSerializer(admins, many=True).data
        return Response(data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "user": serializer.data,
                #"token": serializer.token
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class user_detail(APIView):

    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet)
        print(snippet.pk)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

