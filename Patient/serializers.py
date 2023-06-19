from Accounts.serializers import UserSerializer
from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('pk','user', 'Physio_Patient',)
        read_only_fields = ('pk',)


class PatientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Patient
        fields = ('user', 'Physio_Patient',)
        read_only_fields = ('id','is_patient',)



    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_patient = True
        user.user_type = 'patient'
        user.save()
        myadmin, created = Patient.objects.update_or_create(user=user,
                                                            Physio_Patient=validated_data.pop('Physio_Patient'))
        return myadmin

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
            'is_patient',
            True
        )
        myuser.user_type = user_data.get(
            'user_type',
            'patient'
        )

        myuser.save()
        instance.user = validated_data.get('user', instance.user)
        instance.Physio_Patient = validated_data.get('Physio_Patient', instance.Physio_Patient)
        instance.save()
        return instance