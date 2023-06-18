
from .serializers import *
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import  permission_classes

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


