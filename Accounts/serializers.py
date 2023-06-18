from django.conf import settings
from Accounts.models import NewUser
from rest_framework.exceptions import ValidationError
from PhysioProj import settings
from django.contrib import auth
from rest_framework import serializers,exceptions

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

    '''
    Use pop() when you need one time validation check & will not use the data further.
•	And use get(), when you need validation check & also save data in database.

    '''
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
    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.Contact = validated_data.get('Contact', instance.Contact)
        instance.Address = validated_data.get('Address', instance.Address)
        #instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.password = validated_data.get('password', instance.password)
        instance.user_type = validated_data.get(
            'user_type',
            'staff'
        )
        instance.set_password(instance.password)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")

        if email and password:
            user = auth.authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data

