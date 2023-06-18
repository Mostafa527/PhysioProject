from django.conf import settings
from Accounts.models import NewUser
from rest_framework.exceptions import ValidationError
from PhysioProj import settings
from rest_framework import exceptions
from django.contrib import auth
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    class Meta:
        model = NewUser
        fields = ('id', 'username','first_name','last_name', 'password', 'password2', 'email','Contact', 'Address', 'is_admin','is_doctor','is_patient', 'user_type')
        read_only_fields = ('id', 'is_admin','is_patient','is_doctor','user_type')
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('password2')
        if password != confirm_password:
            raise ValidationError("Passwords doesn't match.")
        return data



    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
            )
        return value




    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')
        Address = validated_data.get('Address')
        #user_type = validated_data.get('user_type')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        Contact =validated_data.get('Contact')
        try:
            user = NewUser.objects.create(username=username,first_name=first_name,last_name=last_name, email=email, Address=Address,Contact=Contact)
            user.user_type = 'staff'
            user.set_password(password)
            user.is_active = True

            user.save()
            return user
        except Exception as e:
            return e