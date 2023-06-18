from Accounts.serializers import UserSerializer
from .models import ClinicAdmin
from rest_framework import serializers

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicAdmin
        fields = ('pk','user', 'Admin_Clinic',)
        read_only_fields = ('pk',)


class AdminProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = ClinicAdmin
        fields = ('user', 'Admin_Clinic',)
        read_only_fields = ('is_admin','id',)



    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data.is_admin=True
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_admin=True
        user.user_type = 'admin'
        user.save()
        myadmin, created = ClinicAdmin.objects.update_or_create(user=user,
                                                            Admin_Clinic=validated_data.pop('Admin_Clinic'))
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
        myuser.is_admin = user_data.get(
            'is_admin',
            True
        )
        myuser.user_type = user_data.get(
            'user_type',
            'admin'
        )

        myuser.save()
        instance.user = validated_data.get('user', instance.user)
        instance.Admin_Clinic = validated_data.get('Admin_Clinic', instance.Admin_Clinic)
        instance.save()
        return instance