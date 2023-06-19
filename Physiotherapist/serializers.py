from Accounts.serializers import UserSerializer
from .models import Physiotherapist
from rest_framework import serializers

class PhysioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physiotherapist
        fields = ('pk','user', 'Clinic_Physio',)
        read_only_fields = ('pk',)


class PhysioProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Physiotherapist
        fields = ('user', 'Clinic_Physio',)
        read_only_fields = ('id','is_doctor',)



    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_doctor = True
        user.user_type = 'doctor'
        user.save()
        physio, created = Physiotherapist.objects.update_or_create(user=user,
                                                            Clinic_Physio=validated_data.pop('Clinic_Physio'))
        return physio

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')


        myuser = instance.user

        myuser.username = user_data.get(
            'username',
            myuser.username
        )

        myuser.email = user_data.get(
            'email',
            myuser.email
        )

        myuser.first_name = user_data.get(
            'first_name',
            myuser.first_name
        )
        myuser.setpassword = user_data.get(
            'password',
            myuser.password
        )
        myuser.is_patient = user_data.get(
            'is_doctor',
            True
        )
        myuser.user_type = user_data.get(
            'user_type',
            'doctor'
        )

        myuser.save()
        instance.user = validated_data.get('user', instance.user)
        instance.Clinic_Physio = validated_data.get('Clinic_Physio', instance.Clinic_Physio)
        instance.save()
        return instance