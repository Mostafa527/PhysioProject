
from .serializers import *
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import  permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication

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

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        django_login(request, user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'is_staff':user.is_staff,
            'is_admin':user.is_admin,
            'is_patient':user.is_patient,
            'is_doctor':user.is_doctor,
            'user_type':user.user_type
        })

#Logout without Delete Token
class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        django_logout(request)
        return Response(status=204)

#Logout and Delete Token
#when Login again it will create a new Token
class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        django_logout(request)
        return Response(status=status.HTTP_200_OK)
